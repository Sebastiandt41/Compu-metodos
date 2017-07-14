import numpy as np 
from numpy import fft
import matplotlib.pyplot as plt
import scipy.io.wavfile 

#Lectura de datos 
rate_viol,data_viol = scipy.io.wavfile.read("violin.wav")

#Transformada de Fourier de Numpy
N = len(data_viol)
dt = 1.0/rate_viol
fft_viol = np.fft.fft(data_viol)
fft_freq = np.fft.fftfreq(len(data_viol),dt)

#Grafica 1 
plt.plot(fft_freq,abs(fft_viol))
plt.xlabel("Frecuencia(Hz)")
plt.xlim([0,10000])
plt.ylabel("Amplitud")
plt.title("Transformada del violin")
plt.savefig("Violin.pdf",format ="pdf")
plt.close()

#Esta funcion elimina todas las frecuencias menores que 1000 Hz y mayores que 2000 Hz
def filtro_pasabanda(datos,freq):
	ampl = np.copy(datos)
	filtro_bajo = 1000
	filtro_alto = 2000
	for i in range(0,N):
		dato = freq[i]
		if (abs(dato) < 1000):
			ampl[i] = 0
		elif(abs(dato)>2000):
			ampl[i] = 0
	return ampl

#Filtramos los datos 
filtro_pb = filtro_pasabanda(fft_viol,fft_freq)

#Grafica 2 
fig,son = plt.subplots(2,1)
son[0].plot(fft_freq,abs(fft_viol),label = "Datos originales")
son[0].legend()
son[0].set_xlim([-7500,7500])
son[0].set_ylabel("Amplitud")
son[1].plot(fft_freq,abs(filtro_pb),c="r",label="Filtro pasabandas")
son[1].legend()
son[1].set_xlim([-7500,7500])
son[1].set_xlabel("Frecuencia(Hz)")
son[1].set_ylabel("Amplitud")
plt.suptitle("Filtro pasabanda")
plt.savefig("ViolinFiltro.pdf",format ="pdf")
plt.close()

def reconstruir_ondas(nombre,datos,rate):
	fft_ix = np.fft.ifft(datos)	
	fft_ix= np.asarray(fft_ix, dtype = np.int32)		
	
	scipy.io.wavfile.write(nombre,rate,fft_ix)	


reconstruir_ondas("Violinfiltered.wav",filtro_pb,rate_viol)
 

















			
