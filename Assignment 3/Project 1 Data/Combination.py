# for example spec-0352-51694-0336 seems to be a 'red' galaxy, over 6500A, it has more flux intensity.
import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

gdata = fits.open('C:/Users/Peter/Desktop/Assignment 3/Project 1/Galaxy Spectra/spec-0352-51694-0336.fits')
plt.plot(10**gdata[1].data['loglam'],gdata[1].data['flux'],'k',lw=0.2)
plt.title('spec-0352-51694-0336.fits')
plt.xlabel('Wavelength[Å]')
plt.ylabel('Flux [10^-17 erg/cm2/s/Å]')
plt.show()


sdata1 = np.loadtxt('C:/Users/Peter/Desktop/Assignment 3/Project 1/Stellar Spectra/ukm3iii.dat',unpack = True)
sdata2 = np.loadtxt('C:/Users/Peter/Desktop/Assignment 3/Project 1/Stellar Spectra/ukk3i.dat',unpack = True)
sdata3 = np.loadtxt('C:/Users/Peter/Desktop/Assignment 3/Project 1/Stellar Spectra/ukg2iv.dat',unpack = True)

wavelen = sdata1[0]
spec1 = sdata1[1]
spec2 = sdata2[1]
spec3 = sdata3[1]
spec = 4*spec1+5*spec2+10*spec3

plt.xlim(3800,9300)
plt.title('combination spectrum')
plt.xlabel('Wavelength[Å]')
plt.ylabel('Flux [erg/cm2/s/Å]')
plt.plot(wavelen,spec)
plt.show()
