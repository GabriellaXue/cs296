import pyaudio
import numpy as np

rate=44100
def get_bit_stream(rate=44100, lambdah=1879.69, duration=3):
    '''
    Function that returns a bit stream with 5 tones at diff. amplitudes.
    '''
    n_frames = int(rate * duration)
    bit_stream = str()
    for x in range(n_frames):
        val = (1 + int((x * 2 * 5) / n_frames)) * (np.sin(x/((rate/lambdah)/np.pi))*127+128)
        bit_stream = bit_stream+chr(int(val))    
    return bit_stream


bit_stream = get_bit_stream()
# TODO: write the bitstream to file.
# Your code here.
controller = pyaudio.PyAudio()
print("runs fine")
stream = controller.open(output = True,
                         rate = 44100,
                         format = pyaudio.paInt16,
                         channels = 1)
stream.start_stream()
stream.write(bit_stream)
stream.stop_stream()
stream.close()
controller.terminate()