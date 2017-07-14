import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import scipy as sci
from scipy import fftpack

imagen_original = plt.imread("moonlanding.png")

fft_ori = np.fft.fft2(imagen_original)

power = (abs(fft_ori))**2
img = plt.imshow(power)
power_cut = 95.0
clipped_power = mlab.prctile(power.flatten(), power_cut)
img.set_clim(0, clipped_power)

def filtro(freq):	
	
	freq[:,50:-50]=0
	freq[50:-50,:]=0
	
	return freq 

spectrum_filtro = filtro(power)
imagen_filtro = filtro(fft_ori)
imagen_filtro1 = np.fft.ifft2(imagen_filtro)
nuevo = (abs(imagen_filtro)**2)

img1 = plt.imshow(spectrum_filtro)
power_cut = 95.0
clipped_power = mlab.prctile(imagen_filtro.flatten(), power_cut)
img1.set_clim(0, clipped_power)
plt.show()
plt.close()


clipped_power = mlab.prctile(nuevo.flatten(), power_cut)
img.set_clim(0, clipped_power)
plt.imshow(nuevo)
plt.show()
plt.close()



plt.imshow(abs(imagen_filtro1))
plt.show()
plt.close()

fig, im = plt.subplots(4,1)
im[0].imshow(imagen_original)
im[0].set_title("Original image")
im[1].imshow(abs(img))
im[1].set_title("Power spectrum")
im[2].imshow(abs(imagen_filtro1))
im[2].set_title("Reconstructed image")
im[3].imshow(nuevo)
im[3].set_title("Filter spectrum")
plt.savefig("2moon_landing.png",format="png")
plt.close()









