import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

def recordSound (sound1):

    samplerate, data = wavfile.read(sound1)
    samples = data.shape[0]
    plt.plot(data[:200])
    # Time domain plot
    #plt.show()
    from scipy.fftpack import fft,fftfreq
    datafft = fft(data)
    fftabs = abs(datafft) # Get the absolute value of real and complex component:
    freqs = fftfreq(samples,1/samplerate)
    plt.plot(freqs,fftabs)
    # Linear Frequency Domain Plot
    #plt.show()
    plt.xlim( [10, samplerate/2] )
    plt.xscale( 'log' )
    plt.grid( True )
    plt.xlabel( 'Frequency (Hz)' )
    plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])
    maxEnergy = np.max(fftabs)
    max_y = maxEnergy  # Find the maximum y value
    max_x = freqs[fftabs.argmax()]  # Find the x value corresponding to the maximum y value
    print ((max_x), " Hz \n", (max_y), " Energy Value")
    # Log Frequency Domain Plot
    #plt.show()
    
recordSound("/home/pi/Desktop/refSound.wav")
