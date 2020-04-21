import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
def recWav(recording):
                        #### Sound Capture
    fs = 44100  # Sample rate
    seconds = 1  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('refSound.wav', fs, myrecording)  # Save as WAV file 
        
recWav("/home/pi/Desktop/refSound.wav")
print("Reference Sound Recorded")

