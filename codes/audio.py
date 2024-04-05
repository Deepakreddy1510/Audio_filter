import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the audio file
sample_rate, data = wavfile.read('audiofiltering.wav')

# Define the function h(n)
def h_n(n, r, p, k):
    sum1 = sum(r[i] * (p[i]**n) for i in range(len(r)))
    sum2 = sum(k[j] if n - j == 0 else 0 for j in range(len(k)))
    return sum1 + sum2

# Define the coefficients r(i), p(i), and k(i)
# You need to define these based on your requirements or analysis of the audio file

# Example coefficients (you should replace these with actual values)
r = np.array([0.5, 0.3, 0.2])
p = np.array([0.9, 0.8, 0.7])
k = np.array([0.1, 0.2, 0.3])

# Create an array for n values
n_values = np.arange(0, len(data))

# Calculate h(n) for each value of n
h_values = np.array([h_n(n, r, p, k) for n in n_values])

# Plot the magnitude of h(n) vs. n using stem plot
plt.stem(n_values, np.abs(h_values), basefmt='k-')
plt.xlabel('n')
plt.ylabel('|h(n)|')
plt.title('Magnitude of h(n)')
plt.grid(True)
plt.show()

