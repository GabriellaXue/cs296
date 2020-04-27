import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def plot_function(v, title="No Title"):
    plt.figure(figsize=(10,5))
    plt.plot(v)
    plt.title(title)
    plt.show()
    
def generate_sin_wave(freq_hz, n_pnts=1000):
    return np.sin(np.linspace(0, 1, (n_pnts)) * 2 * np.pi * freq_hz)

sum_of_3_sin = generate_sin_wave(10) + generate_sin_wave(50) + generate_sin_wave(100)

plot_function(sum_of_3_sin, "3 sin waves with freq: 100, 500, 600")

#window = np.hamming(sum_of_3_sin.size)
#result = window * sum_of_3_sin
finalResult = np.fft.fft(sum_of_3_sin, 1000)
#print(finalResult)
plot_function(finalResult, "Desired Output after DFT")