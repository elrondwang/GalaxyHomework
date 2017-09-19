import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

data = open('Skyserver_Radial9-19-2017 5-38-59 AM.csv','r')

u = pd.read_csv(filepath_or_buffer = 'Skyserver_Radial9-19-2017 5-38-59 AM.csv', sep = ',')['u'].values
g = pd.read_csv(filepath_or_buffer = 'Skyserver_Radial9-19-2017 5-38-59 AM.csv', sep = ',')['g'].values
r = pd.read_csv(filepath_or_buffer = 'Skyserver_Radial9-19-2017 5-38-59 AM.csv', sep = ',')['r'].values

print(u)
print(g)
print(r)
u_g = u-g
g_r = g-r
x=np.arange(-6,8,0.02)
y=2.2-x

plt.figure(figsize=(9,6))
plt.plot(x,y,'r')
plt.plot(u_g,g_r,'ko',ms=3)
plt.xlabel('u-g')
plt.ylabel('g-r')
plt.title('Abell 2255 color-color diagram')

plt.savefig('Abell 2255 color-color diagram.png')
plt.show()