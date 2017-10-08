import matplotlib.pyplot as plt
from astropy.io import fits
import os.path

file = os.listdir(r'C:/Users/Peter/Desktop/Assignment 3/Project 1/Galaxy Spectra')

speca = []
for s in file:
    speca.append(fits.open('C:/Users/Peter/Desktop/Assignment 3/Project 1/Galaxy Spectra/'+s))

i = 0
for a in speca:
    plt.plot(10**a[1].data['loglam'],a[1].data['flux'],'k',lw=0.2)
    plt.title(file[i])
    plt.xlabel('Wavelength[Å]')
    plt.ylabel('Flux [10^-17 erg/cm2/s/Å]')
    plt.show()
    i += 1
