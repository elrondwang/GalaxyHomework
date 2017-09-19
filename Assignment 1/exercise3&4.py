import matplotlib.pyplot as plt
import pandas as pd
import csv

data = open('notebook.csv','r')

u = pd.read_csv(filepath_or_buffer = 'notebook.csv', sep = ',')['u'].values
g = pd.read_csv(filepath_or_buffer = 'notebook.csv', sep = ',')['g'].values
r = pd.read_csv(filepath_or_buffer = 'notebook.csv', sep = ',')['r'].values

u_g = u-g
g_r = g-r

plt.figure(figsize=(9,6))
plt.plot(u_g,g_r,'ko',ms=3)
plt.xlabel('u-g')
plt.ylabel('g-r')
plt.title('color-color diagram')

plt.savefig('color-color diagram.png')
plt.show()