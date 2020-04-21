## This file continuously samples and compares to reference recording from refCapture.py

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
import wave
sens = 0.05 # Sensitivity

#### Captures and Analyzes Recording of Sample Sound
def recAndSpec(sampRecording):
                        #### Sound Capture ####
    fs = 44100  # Sample rate
    seconds = 0.05  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('sampleSound.wav', fs, myrecording)  # Save as WAV file 

                        ####  Sound Analysis ####
    samplerate, data = wavfile.read(sampRecording)
    samples = data.shape[0]
    plt.plot(data[:200])  # Create plot to analyze frequency contents
    from scipy.fftpack import fft,fftfreq  # Perform FFT on sample sound
    datafft = fft(data)   
    fftabs = abs(datafft) #Get the absolute value of real and complex component
    freqs = fftfreq(samples,1/samplerate)
    plt.plot(freqs,fftabs) # Linear Frequency Domain Plot
    plt.xlim( [10, samplerate/2] )
    plt.xscale( 'log' )
    plt.grid( True )
    plt.xlabel( 'Frequency (Hz)' )
    plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)]) # Log Frequency Domain Plot
    maxEnergy = np.max(fftabs)
    max_y = maxEnergy  # Find the maximum y value
    max_x = freqs[fftabs.argmax()]  # Find the x value corresponding to the maximum y value
    #print ((max_x), " Hz \n", (max_y), " Energy Value")
    return max_x
    
####               Analyzes refSound.wav recorded in refCapture.py
def refSpec(refRec):
    samplerate, data = wavfile.read(refRec)
    samples = data.shape[0]
    plt.plot(data[:200]) # Time domain plot
    from scipy.fftpack import fft,fftfreq # Perform FFT on reference sound
    datafft = fft(data)
    fftabs = abs(datafft)  # Get the absolute value of real and complex component:
    freqs = fftfreq(samples,1/samplerate)
    plt.plot(freqs,fftabs) # Linear Frequency Domain Plot
    plt.xlim( [10, samplerate/2] )
    plt.xscale( 'log' )
    plt.grid( True )
    plt.xlabel( 'Frequency (Hz)' )
    plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)]) # Log Frequency Domain Plot
    maxEnergy = np.max(fftabs)
    refmax_y = maxEnergy  # Find the maximum y value
    refmax_x = freqs[fftabs.argmax()]  # Find the x value corresponding to the maximum y value
    #print ((refmax_x), " Hz \n", (refmax_y), " Energy")
    return refmax_x

sampFundFreq = (recAndSpec("/home/pi/Desktop/sampleSound.wav"))
refFundFreq = (refSpec("/home/pi/Desktop/refSound.wav"))

# Loop to continuously sample until sample frequency is within sens range around reference
while sampFundFreq < (refFundFreq - (refFundFreq * sens)) or sampFundFreq > (refFundFreq + (refFundFreq * sens)):
   recAndSpec("/home/pi/Desktop/sampleSound.wav")
   sampFundFreq = recAndSpec("/home/pi/Desktop/sampleSound.wav")
   #print(sampFundFreq, "Hz")
else:
    print("Detected the frequency, at",(sampFundFreq),"Hz")

 