import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import pyaudio
from scipy.signal import butter, filtfilt

fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(0, 2), ylim=(0, 2))

base = plt.Circle((1, 1), 0.2, fc='b')

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 4096

controller = pyaudio.PyAudio()
stream = controller.open(format = FORMAT,
                         input = True,
                         channels = CHANNELS,
                         rate = RATE,
                         frames_per_buffer = FRAMES_PER_BUFFER)

def init():
    ax.add_patch(base)
    return base,

def loop(i):
    
    sample = stream.read(FRAMES_PER_BUFFER, exception_on_overflow = False)
    data = np.fromstring(sample, dtype=np.int16).astype(np.float32)
    # <- @TODO replace this line with code to read a sample from the microphone.
    if sum(sample) > 0:
        
#         nyq = 0.5 * FRAMES_PER_BUFFER
#         b, a = butter(2, [60/ nyq, 250 / nyq], btype = "band", analog = True)
#         y = filtfilt(b, a, sample)
#         print("This is y")
#         print(y)

        window = np.hamming(data.size)
        result = window * data
        finalResult = np.fft.rfft(result, FRAMES_PER_BUFFER)
        log_scale = 10 ** np.arange(0, np.log10(len(finalResult) + 1))
        indices = []
        
        for i in range(1, len(log_scale)) :
            indices.append(int(np.sqrt(log_scale[i-1] * log_scale[i])))
        bins = np.split(finalResult, indices)
        list = []
        for elem in bins:
            for i in range(0, len(elem)):
                list.append(elem[i])
        bins = np.array(list)
        calc_base = np.mean(bins)
        print(calc_base)
        # <- @TODO replace this line with processed signal.
        base.set_radius(calc_base)
    return base,


anim = animation.FuncAnimation(fig, loop, 
                               init_func=init, 
                               frames=10, 
                               interval=10,
                               blit=True)
plt.xlim(-500, 500)
plt.ylim(-500, 500)
plt.show()
