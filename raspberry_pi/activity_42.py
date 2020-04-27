import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
#from IPython import get_ipython

#display a seperate window
#%matplotlib tk
#get_ipython().run_line_magic('matplotlib', 'qt')

#how many audio per frame is going to be played
CHUNK = 512
#bytes per sample
FORMAT = pyaudio.paInt16
CHANNELS = 1
#samples per second
RATE = 44100

#main pyaudio object
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = CHUNK)

fig, ax = plt.subplots()

x = np.arange(0, 2 * CHUNK, 20)
line, = ax.plot(x, np.random.rand(int(CHUNK/10) + 1))
ax.set_xlim(0, CHUNK)
ax.set_ylim(0, 255)

while True:
    data = stream.read(CHUNK)
    #data = np.fromstring(stream_data, dtype=np.int16).astype(np.float32)
    
    #convert to a tuple with all the integers from 0 to 255
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype = 'b')[::20] + 127
    window = np.hamming(len(data_int))
    result = window * data_int
    line.set_ydata(result)
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()
#ax.plot(data_int, "-")
#plt.show()