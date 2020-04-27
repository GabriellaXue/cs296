import pyaudio
import numpy as np
from numpy.linalg import norm

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
        print(norm(data))
    except KeyboardInterrupt:
        break

print('\nShutting down')

# TODO: Step (3) close stream
stream.close()
controller.terminate()