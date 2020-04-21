import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
import wave

#### Captures and Analyzes Recording
def recAndSpec(recording):
                        #### Sound Capture
    fs = 44100  # Sample rate
    seconds = 0.1  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('refSound.wav', fs, myrecording)  # Save as WAV file 

                        ####  Sound Analysis
    samplerate, data = wavfile.read(recording)
    samples = data.shape[0]

    plt.plot(data[:200])
#plt.show()
    from scipy.fftpack import fft,fftfreq
    datafft = fft(data)
#Get the absolute value of real and complex component:
    fftabs = abs(datafft)
#print(fftabs)
    freqs = fftfreq(samples,1/samplerate)
    plt.plot(freqs,fftabs)
#plt.show()
    plt.xlim( [10, samplerate/2] )
    plt.xscale( 'log' )
    plt.grid( True )
    plt.xlabel( 'Frequency (Hz)' )
    plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])
    maxEnergy = np.max(fftabs)
    max_y = maxEnergy  # Find the maximum y value
    max_x = freqs[fftabs.argmax()]  # Find the x value corresponding to the maximum y value
    #print ((max_x), " Hz \n", (max_y), " Energy")
    return max_x
    #plt.show()

fundFreq = 0;
while fundFreq < 755 or fundFreq > 770:
    recAndSpec("/home/pi/Desktop/refSound.wav")
    fundFreq = recAndSpec("/home/pi/Desktop/refSound.wav")
    print(fundFreq)
else:
    print("Detected the microwave!, at",(fundFreq),"Hz")
    plt.show()

"""
fundFreq = recAndSpec("/home/pi/Desktop/output22.wav")
if fundFreq > 400:
    print("Over 400!, at",(fundFreq),"Hz")
else:
    recAndSpec("/home/pi/Desktop/output22.wav")
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
import wave

## Sound Capture

fs = 44100  # Sample rate
seconds = 1  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output22.wav', fs, myrecording)  # Save as WAV file 

##  Sound Analysis

samplerate, data = wavfile.read("/home/pi/Desktop/output22.wav")
# print (samplerate)
# print (data.shape)
samples = data.shape[0]
#print (samples)
plt.plot(data[:200])
#plt.show()

from scipy.fftpack import fft,fftfreq
datafft = fft(data)
#print(datafft)
#Get the absolute value of real and complex component:
fftabs = abs(datafft)
#print(fftabs)

freqs = fftfreq(samples,1/samplerate)

plt.plot(freqs,fftabs)
#plt.show()

plt.xlim( [10, samplerate/2] )
plt.xscale( 'log' )
plt.grid( True )
plt.xlabel( 'Frequency (Hz)' )
plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])

maxEnergy = np.max(fftabs)
max_y = maxEnergy  # Find the maximum y value
max_x = freqs[fftabs.argmax()]  # Find the x value corresponding to the maximum y value
print ((max_x), " Hz \n", (max_y), " Energy")
#plt.show()

if max_x < 400 and max_x > 300:
    match = true
"""