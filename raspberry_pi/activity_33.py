import pyaudio
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
import statistics
import math

def plot_function(v, title="No Title"):
    plt.figure(figsize=(10,5))
    plt.plot(v)
    plt.title(title)
    plt.show()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 4096

controller = pyaudio.PyAudio()

# TODO: Step (1) open stream
stream = controller.open(format = FORMAT,
                         input = True,
                         channels = CHANNELS,
                         rate = RATE,
                         frames_per_buffer = FRAMES_PER_BUFFER)

while True:
    try:
        # TODO: Step (2) read from stream
        stream_data = stream.read(FRAMES_PER_BUFFER) # <-- TODO: Change this!
        data = np.fromstring(stream_data, dtype=np.int16).astype(np.float32)
#         window = np.hamming(data.size)
#         result = window * data
#         finalResult = np.fft.fft(result, 1000)
#         plot_function(finalResult, "Desired Output after DFT")
#         print("working")
        log_scale = 10 ** np.arange(0, np.log10(len(data) + 1))
        indices = []
        for i in range(1, len(log_scale)) :
            indices.append(int(np.sqrt(log_scale[i-1] * log_scale[i])))
        indices = [0] + indices + [len(data)]
        bins = np.split(data, indices)
    except KeyboardInterrupt:
        break
    


# TODO: Step (3) close stream
stream.close()
controller.terminate()

