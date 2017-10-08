import matplotlib.pyplot as plt
import numpy as np
import os.path

file = os.listdir(r'C:/Users/Peter/Desktop/Assignment 3/Project 1/Stellar Spectra')

speca = []
for s in file:
    speca.append(np.loadtxt('C:/Users/Peter/Desktop/Assignment 3/Project 1/Stellar Spectra/'+s,unpack=True))

i = 0
for a in speca:
    plt.xlim(3800,9300)
    plt.plot(a[0],a[1],'k',lw=0.5)
    plt.title(file[i])
    plt.xlabel('Wavelength[Å]')
    plt.ylabel('Flux [erg/cm2/s/Å]')
    plt.show()
    i += 1
