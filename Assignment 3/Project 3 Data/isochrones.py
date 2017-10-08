import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = np.loadtxt('isocz019.dat',unpack=True)
galaxy = open('notebook.csv','r')

u = pd.read_csv(filepath_or_buffer = 'notebook.csv', sep = ',')['u'].values
g = pd.read_csv(filepath_or_buffer = 'notebook.csv', sep = ',')['g'].values
r = pd.read_csv(filepath_or_buffer = 'notebook.csv', sep = ',')['r'].values 

logage = data[0]
Mu = data[7]
Mv = data[9]
Mr = data[10]

u_g = Mu-Mv
g_r = Mv-Mr

U_G = u-g
G_R = g-r

plt.plot(U_G,G_R,'ro',ms=3)
plt.plot(u_g,g_r,'ko',ms=0.5)
plt.xlabel('u-g')
plt.ylabel('g-r')
plt.title('c-c diagram')
