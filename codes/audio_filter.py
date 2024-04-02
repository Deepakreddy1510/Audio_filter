import soundfile as sf
from scipy import signal

input_signal,fs = sf.read('audiofiltering.wav') 


sampl_freq=fs

order=4

cutoff_freq=1000.0  

Wn=2*cutoff_freq/sampl_freq  

b, a = signal.butter(order, Wn, 'low') 

output_signal = signal.lfilter(b, a, input_signal)

sf.write('Sound_With_ReducedNoise.wav', output_signal, fs) 
