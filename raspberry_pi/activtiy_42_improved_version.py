import pyaudio
import numpy
import math
import matplotlib.pyplot as plt
import matplotlib.animation

RATE = 44100
BUFFER = 1024

p = pyaudio.PyAudio()

stream = p.open(
    format = pyaudio.paFloat32,
    channels = 1,
    rate = RATE,
    input = True,
    output = False,
    frames_per_buffer = BUFFER
)

fig = plt.figure()
line = plt.plot([],[])[0]

x = range(0,int(RATE/2+1),int(RATE/BUFFER))
l = len(x)

def init_line():
        line.set_data(x, [0]*l)
        return line,

def update_line(i):
    try:
        stream_data = numpy.fromstring(stream.read(BUFFER), dtype=numpy.float32)
        window = numpy.hamming(len(stream_data))
        data = window * stream_data
        data = numpy.fft.rfft(data)
    except IOError:
        pass
#     data = numpy.log10(numpy.sqrt(numpy.real(data)**2+numpy.imag(data)**2) / BUFFER) * 10
    log_scale = 10 ** numpy.arange(0, numpy.log10(len(data) + 1))
    indices = []  
    for i in range(1, len(log_scale)) :
        indices.append(int(numpy.sqrt(log_scale[i-1] * log_scale[i])))
    bins = numpy.split(data, indices)
    list = []
    for elem in bins:
        for i in range(0, len(elem)):
            list.append(elem[i])
    bins = numpy.array(list)
    line.set_data(x, bins)
    return line,

plt.xlim(0, 2000)
plt.ylim(-60, 60)
plt.xlabel('Frequency')
plt.ylabel('signal')
plt.title('audio visualization')
plt.grid()

line_ani = matplotlib.animation.FuncAnimation(
    fig, update_line, init_func=init_line, interval=0, blit=True
)

plt.show()