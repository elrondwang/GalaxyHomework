import matplotlib.pyplot as plt
import pandas as pd

data = open('Data.csv','r')
B_V = pd.read_csv(filepath_or_buffer = 'Data.csv',sep =',')['B-V'].values
U_B = pd.read_csv(filepath_or_buffer = 'Data.csv',sep =',')['U-B'].values
Fraction = pd.read_csv(filepath_or_buffer = 'Data.csv',sep =',')['Fraction(%)'].values

# phase 1
phase1B_V = sum(B_V * Fraction)/sum(Fraction)
phase1U_B = sum(U_B * Fraction)/sum(Fraction)

# phase 2
B_V = B_V[1:]
U_B = U_B[1:]
Fraction = Fraction[1:]
phase2B_V = sum(B_V * Fraction)/sum(Fraction)
phase2U_B = sum(U_B * Fraction)/sum(Fraction)

# phase 3
B_V = B_V[1:]
U_B = U_B[1:]
Fraction = Fraction[1:]
phase3B_V = sum(B_V * Fraction)/sum(Fraction)
phase3U_B = sum(U_B * Fraction)/sum(Fraction)

# phase 4
B_V = B_V[1:]
U_B = U_B[1:]
Fraction = Fraction[1:]
phase4B_V = sum(B_V * Fraction)/sum(Fraction)
phase4U_B = sum(U_B * Fraction)/sum(Fraction)

# phase 5
B_V = B_V[1:]
U_B = U_B[1:]
Fraction = Fraction[1:]
phase5B_V = sum(B_V * Fraction)/sum(Fraction)
phase5U_B = sum(U_B * Fraction)/sum(Fraction)

# phase 6
B_V = B_V[1:]
U_B = U_B[1:]
Fraction = Fraction[1:]
phase6B_V = sum(B_V * Fraction)/sum(Fraction)
phase6U_B = sum(U_B * Fraction)/sum(Fraction)

# phase 7
B_V = B_V[1:]
U_B = U_B[1:]
Fraction = Fraction[1:]
phase7B_V = sum(B_V * Fraction)/sum(Fraction)
phase7U_B = sum(U_B * Fraction)/sum(Fraction)

b_v = [phase1B_V,phase2B_V,phase3B_V,phase4B_V,phase5B_V,phase6B_V,phase7B_V]
u_b = [phase1U_B,phase2U_B,phase3U_B,phase4U_B,phase5U_B,phase6U_B,phase7U_B]

plt.figure(figsize=(12,8))
plt.plot(b_v,u_b,'ko',ms=3)
plt.xlabel('B-V')
plt.ylabel('U-B')
plt.title('SSP')
plt.savefig('color evolution.png')