import pyaudio
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift

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

def plot_function(v, title="No Title"):
    plt.figure(figsize=(10,5))
    plt.plot(v)
    plt.title(title)
    plt.show()

while True:
    try:
        stream_data = stream.read(FRAMES_PER_BUFFER)
        data = np.fromstring(stream_data, dtype=np.int16).astype(np.float32)
        print(norm(data))
        window = np.hamming(data.size)
        result = window * data
        print("working")
        finalResult = np.fft.fft(result, FRAMES_PER_BUFFER)
        plot_function(finalResult, "Desired Output after DFT")
    except KeyboardInterrupt:
        break
    


# TODO: Step (3) close stream
stream.close()
controller.terminate()
