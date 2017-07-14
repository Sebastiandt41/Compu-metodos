import numpy as np 
from numpy import fft 
import matplotlib.pyplot as plt
import scipy.io.wavfile

rate_Do,data_Do = scipy.io.wavfile.read("Do.wav")
rate_Sol,data_Sol = scipy.io.wavfile.read("Sol.wav")

dt = 1.0/rate_Sol
fft_Sol = np.fft.fft(data_Sol)
freq_Sol = np.fft.fftfreq(len(data_Sol),dt)

print dt
new_rate = (rate_Do+8126.0)
dt1 = 1.0/new_rate
fft_Do = np.fft.fft(data_Do)
freq_Do = np.fft.fftfreq(len(data_Do),dt1)
print rate_Do
print dt1

plt.plot(freq_Sol,abs(fft_Sol),color = "r")
plt.plot(freq_Do,abs(fft_Do),color="b")
plt.xlim([0,8000])
plt.show()
plt.close()

def reconstruir_ondas(sol):
	Do_1 = np.fft.ifft(sol)	
	Do_1 = np.asarray(sol ,dtype = np.int16)	
	
	scipy.io.wavfile.write("Do_Sol.wav",new_rate,Do_1)
	print new_rate
	

reconstruir_ondas(fft_Do)
