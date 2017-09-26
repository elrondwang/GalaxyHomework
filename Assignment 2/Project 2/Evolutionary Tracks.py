import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

Ms = 4.83

data1 = np.loadtxt('outputiso466921330270.dat',unpack=True)
T = data1[2]
L = data1[1]

data2 = open('List of brightest stars.csv','r')
BV = pd.read_csv(filepath_or_buffer = 'List of brightest stars.csv', sep = ',')['B-V'].values
M = pd.read_csv(filepath_or_buffer = 'List of brightest stars.csv', sep = ',')['M'].values
Name=pd.read_csv(filepath_or_buffer = 'List of brightest stars.csv', sep = ',')['name'].values

Ts = np.log10(4600*(1/(0.92*BV+1.7)+1/(0.92*BV+0.62)))
Ls = (Ms-M)/2.5


plt.figure(figsize=(8,8))
plt.gca().invert_xaxis()

plt.plot(T,L,'co',ms=0.5)
plt.plot(Ts,Ls,'ro',ms=3.5)
for i in range(0,20):
    if (i != 16) and (i != 3) and (i != 18):
        plt.annotate(Name[i], xy = (Ts[i]-0.01, Ls[i]-0.01), fontsize=9)
    elif i == 16:
        plt.annotate(Name[i], xy = (Ts[i], Ls[i]-0.2), fontsize=9)
    elif i == 3:
        plt.annotate(Name[i], xy = (Ts[i]+0.08, Ls[i]+0.1), fontsize=9)
    else:
        plt.annotate(Name[i], xy = (Ts[i]+0.1, Ls[i]-0.18), fontsize=9)

plt.xlabel('LogTe')
plt.ylabel('Log(L/L0)')

plt.savefig('Evolutionary Tracks.png')
plt.show()