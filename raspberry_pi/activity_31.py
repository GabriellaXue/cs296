import numpy as np
from scipy.signal import butter, lfilter, filtfilt
import matplotlib.pyplot as plt
import math

def plot_function(v, title="No Title"):
    plt.figure(figsize=(10,5))
    plt.plot(v)
    plt.title(title)
    plt.show()
    
def generate_sin_wave(freq_hz, n_pnts=1000):
    return np.sin(np.linspace(0, 1, (n_pnts)) * 2 * np.pi * freq_hz)

sum_of_3_sin = generate_sin_wave(5) + generate_sin_wave(50) + generate_sin_wave(100)

plot_function(sum_of_3_sin, "3 sin waves with freq: 5, 50, 100")

def filter_low_and_high(signal, order=2):
    # @TODO: implement this.
    nyq = 0.5 * 1000
    low = 49 / nyq
    high = 51 / nyq
    b, a = butter(5, high, btype='low')
    y = filtfilt(b, a, signal)
    #low1 = 51 / nyq
    #high1 = 99 / nyq
    c, d = butter(5, low, btype='high')
    z = filtfilt(c, d, y)
    return z

filtered_50_hz_sin = filter_low_and_high(sum_of_3_sin)  
plot_function(filtered_50_hz_sin, "Desired Output")
