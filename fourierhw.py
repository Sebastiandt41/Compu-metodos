import numpy as np 
from numpy import fft 
import matplotlib.pyplot as plt
import scipy.io.wavfile

rate_Do,data_Do = scipy.io.wavfile.read("Do.wav")
rate_Sol,data_Sol = scipy.io.wavfile.read("Sol.wav")

data_Do=data_Do[0:16000]
data_Sol=data_Sol[0:16000]

N_Do = len(data_Do)
N_Sol = len(data_Sol)


#Transformada de fourier manual
def transformada_manual(datos,rate):
	larg_float = float(len(datos))
	freq_manual =[]
	fft_manual=[]		
	for n in range (0,len(datos)):		
		ffts = 0
		valor_freq =(n/larg_float)*rate			
		for k in range(0,len(datos)):			
			ffts += datos[k]*np.exp(-1j*2.0*(np.pi)*k*(n/larg_float))

		fft_manual.append(ffts)		
		freq_manual.append(valor_freq)	
	fft_manual = np.asarray(fft_manual)
	freq_manual = np.asarray(freq_manual)
	return fft_manual	

#Transformadas de fourier numpy	
dt_Do = 1.0/rate_Do
dt_Sol = 1.0/rate_Sol
fft_realDo = np.fft.fft(data_Do)
fft_realSol = np.fft.fft(data_Sol)
fft_freqDo = np.fft.fftfreq(N_Do,dt_Sol)
fft_freqSol = np.fft.fftfreq(N_Sol,dt_Sol)

#Transformadas manuales

fft_manualDo = transformada_manual(data_Do,rate_Do)
fft_manualSol = transformada_manual(data_Sol,rate_Sol)

#Prueba que la transformada manual esta bien

#x = np.real(fft_manualDo)/np.real(fft_realDo)
#print x 

#Funcion filtro que elimina la frecuencia con mayor amplitud 
def filtro_ampl(datos,freq):
	
	ampl = np.copy(datos)
	frequ = np.copy(freq)
	max_ampl=0
	contador_fftx = 0
	contador = 0
	rm_22 = 0
	k = len(ampl)
	for i in range(0,k):
		dato = abs(ampl[i])
		freq_i = frequ[i]
		if(dato>max_ampl):
			max_ampl = dato
			contador_fftx = i
		elif(freq_i == 0) :
			contador = i
	rm = contador - contador_fftx	
	rm_22 = contador_fftx+2*(rm)		
	ampl[contador_fftx]=0
	ampl[rm_22] = 0
	
	for j in range(contador_fftx-20,contador_fftx+20):
		ampl[j] = 0
	for k in range(rm_22-20,rm_22+20):
		ampl[k] = 0	
	
	return ampl

#Funcion filtro que elimina las frecuencias mayores a 1000 Hz 

def filtro_pasabajos(datos,freq):	
	ampl = np.copy(datos)
	frequ= np.copy(freq)
	freq_cut = 1000
	for i in range(0,len(ampl)):		
		dato = abs(frequ[i])
		if (dato > freq_cut):
			ampl[i] = 0
	return  ampl

#Filtramos los datos 
#filtro_1 = filtro_ampl(fft_realDo,fft_freqDo)
filtro_1 = filtro_ampl(fft_manualDo,fft_freqDo)
#filtro_2 = filtro_pasabajos(fft_realDo,fft_freqDo)
filtro_2 = filtro_pasabajos(fft_manualDo,fft_freqDo)

#Funcion que calcula la transformada inversa de fourier y reconstruye la onda de sonido.

def reconstruir_ondas(nombre,datos,rate):
	fft_ix = np.fft.ifft(datos)	
	fft_ix= np.asarray(fft_ix, dtype = np.int16)		
	
	scipy.io.wavfile.write(nombre,rate,fft_ix)	

reconstruir_ondas("Do_pico.wav",filtro_1,rate_Do)
reconstruir_ondas("Do_pasabajos.wav",filtro_2,rate_Do)

#Grafica de los filtros de Do

fig,sonidos = plt.subplots(3,1)
sonidos[0].plot(fft_freqDo , abs(fft_manualDo),c="r",label="Datos originales")
#sonidos[0].set_xlim([0,8000])
sonidos[0].legend()
sonidos[1].plot(fft_freqDo , abs(filtro_1),c="g",label="Filtro mayor amplitud")
#sonidos[1].set_xlim([0,8000])
sonidos[1].legend()
sonidos[2].plot(fft_freqDo , abs(filtro_2),c="c",label="Filtro pasabajos")
#sonidos[2].set_xlim([0,8000])
sonidos[2].legend()
plt.suptitle("Do.wav filters")
plt.savefig("DoFiltros.pdf",format ="pdf")
plt.show()
plt.close()	


#De Do a Sol

fre_Do = 260.0
fre_Sol = 391.0 
factor = fre_Sol/fre_Do
new_rate = rate_Do*factor
new_rate_int = int(rate_Do*factor)

scipy.io.wavfile.write("DoSol.wav",new_rate_int,data_Do)


#Grafica Do - Sol 

dt1 = 1.0/new_rate
freq_DoSOl = np.fft.fftfreq(N_Do,dt1)

figu,son = plt.subplots(3,1)
son[0].plot(fft_freqSol,abs(fft_manualSol),label="Sol real")
son[0].set_xlim([-8000,8000])
son[0].legend()
son[1].plot(freq_DoSOl,abs(fft_manualDo),label="Sol artificial",color="r")
son[1].set_xlim([-8000,8000])
son[1].legend()
son[2].plot(fft_freqSol,abs(fft_manualSol),label="Sol real")
son[2].plot(freq_DoSOl,abs(fft_manualDo),label="Sol artificial",color="r")
son[2].set_xlim([-8000,8000])
son[2].legend()
plt.suptitle("Do-Sol")
plt.savefig("DoSol.pdf",format="pdf")
plt.show()
plt.close()














		
			

