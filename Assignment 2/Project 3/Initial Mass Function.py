import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

hdu = fits.open('The Hipparcos Main Catalogue.fit')
hdu.info()
hdu[0].header

#1pc~100pc
Plx1 = (hdu[1].data['Plx']>10)
Plx2 = (hdu[1].data['Plx']<1000)
Plxs = Plx1*Plx2
dat = hdu[1].data[Plxs]

S = dat['Plx']/1000
Mv = 5+dat['Vmag']+5*np.log10(S)

n = plt.hist(Mv,14,range=(-2,12),ls='--',histtype='step')
plt.close()

plt.figure(figsize=(10,7))
V = 4/3*np.pi*(100**3-1**3)
x = n[1][0:len(n[1])-1]+0.5
y = np.log10(n[0][0:]/V)+10
plt.plot(x, y,'k')

plt.xlabel('Mv')
plt.ylabel('log $\phi$(M)+10')
plt.savefig('IMF.png')
plt.show()