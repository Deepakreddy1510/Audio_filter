import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = np.zeros_like(data, dtype=np.float64)
    for i in range(len(data)):
        for j in range(1, order+1):
            if i-j >= 0:
                y[i] += b[j] * data[i-j]
        for j in range(order):
            if i-j-1 >= 0:
                y[i] -= a[j+1] * y[i-j-1]
        y[i] /= a[0]
    return np.int16(y)

# Parameters
input_file = "audiofiltering.wav"
output_file_builtin = "audio_filtered_builtin.wav"
output_file_custom = "audio_filtered_custom.wav"
cutoff_frequency = 1000  # Hz
order = 4
max_time = 5  # seconds

# Read the audio file
fs, data = wav.read(input_file)

# Trim audio to max_time seconds
max_samples = int(max_time * fs)
data = data[:max_samples]

# Filter the data using inbuilt function
b, a = butter_lowpass(cutoff_frequency, fs, order)
filtered_data_builtin = lfilter(b, a, data).astype(np.int16)
wav.write(output_file_builtin, fs, filtered_data_builtin)

# Filter the data using custom function
filtered_data_custom = butter_lowpass_filter(data, cutoff_frequency, fs, order)
wav.write(output_file_custom, fs, filtered_data_custom)

# Time axis
time = np.arange(0, len(data)) / fs

# Plot
plt.figure(figsize=(10, 6))

# Plot filtered audio using inbuilt function
plt.plot(time, filtered_data_builtin, label='Filtered (Using Built-in)', alpha=0.7)

# Plot filtered audio using custom function
plt.plot(time, filtered_data_custom, label='Filtered (Without Built-in)', alpha=0.7)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Filtered Audio Comparison')
plt.legend()
plt.grid(True)
plt.show()
