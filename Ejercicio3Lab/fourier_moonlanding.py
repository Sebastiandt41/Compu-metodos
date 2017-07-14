import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import scipy as sci
from scipy import fftpack

imagen_original = plt.imread("moonlanding.png")
#Imagen original 
plt.imshow(imagen_original)
plt.title("Original image")
plt.savefig("Imagen original",format="png")
plt.close()

fft_ori = np.fft.fft2(imagen_original)
#Espectro de poder
power = (abs(fft_ori))**2
img = plt.imshow(power)
power_cut = 95.0
clipped_power = mlab.prctile(power.flatten(), power_cut)
img.set_clim(0, clipped_power)
plt.title("Power spectrum")
plt.savefig("Power spectrum",format="png")
plt.close()

def filtro(freq):	
	
	freq[:,50:-50]=0
	freq[50:-50,:]=0
	
	return freq 

power_filtro = filtro(power)

#Reconstruir imagen filtrada 
imagen_filtro = filtro(fft_ori)
imagen_filtro1 = np.fft.ifft2(imagen_filtro)
plt.imshow(abs(imagen_filtro1))
plt.title("Reconstructed image")
plt.savefig("Reconstructed image",format="png")
plt.close()

#Imagen del espectro de poder filtrado 
power_filter = (abs(imagen_filtro))**2
img1 = plt.imshow(power_filter)
power_cut = 95.0
clipped_power = mlab.prctile(power_filter.flatten(), power_cut)
img.set_clim(0, clipped_power)
plt.title("Filtered spectrum")
plt.savefig("Filtered spectrum",format="png")
plt.close()

fig,sub = plt.subplots(2,2)
sub[0,0].imshow(imagen_original)
sub[0,0].set_title("Imagen original")
sub[0,1].imshow(power)
sub[0,1].set_title("Power spectrum")
sub[1,0].imshow(abs(imagen_filtro1))
sub[1,0].set_title("Reconstructed image")
sub[1,1].imshow(power_filter)
sub[1,1].set_title("Filtered spectrum")
plt.savefig("Moon_landing",format="png")
plt.close()















