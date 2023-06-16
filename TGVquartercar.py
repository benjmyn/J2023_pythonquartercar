
import os, random
os.system('cls')
print("----------------------------------------\n           Quarter-Car Model:\n----------------------------------------")
import numpy as np
# from numpy import loadtxt
from matplotlib import pyplot as plt
np.set_printoptions(precision=5, sign='+', suppress=True, floatmode='fixed')

num = 100
z0 = np.zeros(num)
#for i in range(2,num):
#    z0[i] = z0[i-1] + random.triangular(-0.001, 0.001, 0)
#    z0[i] = z0[i-1] + random.triangular(0.03+z0[0] - z0[i]/2, -(0.03+z0[0]) - z0[i]/2, z0[0])
#print(z0)

z0[2] = .001

z1 = np.zeros(num)
v1 = np.zeros(num)
a1 = np.zeros(num)
z2 = np.zeros(num)
v2 = np.zeros(num)
a2 = np.zeros(num)

V = 80 / 3.6
dt = 1/V

zeta = 0.3
k_tr = 176000.0
k_s = k_tr/8
m_s = 454.5
m_us = 0.10*m_s

c_sh = 2*np.sqrt(k_s*m_s) * zeta
#print(c_sh)
#c_sh = 0

A = c_sh*dt/2 + k_s*(dt**2)/6
B = m_s + c_sh*dt/2 + k_s*(dt**2)/6
C = m_us + c_sh*dt/2 + (k_s + k_tr)*(dt**2)/6

a1[1] = (k_tr*z0[1]*A) / (B*C - A**2)
a2[1] = (a1[1]*B) / A
v1[1] = a1[1]*dt/2
v2[1] = a2[1]*dt/2
z1[1] = v1[1]*dt/3
z2[1] = v2[1]*dt/3

for i in range(2,num):
    z1[i] = a1[i-1]*(dt**2) + 2*v1[i-1] - z1[i-2]
    z2[i] = a2[i-1]*(dt**2) + 2*v2[i-1] - z2[i-2]
    
    v1[i] = (3*z1[i] - 4*z1[i-1] + z1[i-2]) / (2*dt)
    v2[i] = (3*z2[i] - 4*z2[i-1] + z2[i-2]) / (2*dt)
    
    a1[i] = ( c_sh*(v2[i] - v1[i]) + k_s*(z2[i] - z1[i]) ) / m_s
    a2[i] = ( k_tr*(z0[i] - z2[i]) - c_sh*(v2[i]-v1[i]) - k_s*(z2[i]-z1[i]) ) / m_us

test = 2
print("Station", test+1) 
print("z**1:", a1[test:test+3], "\nz**2:", a2[test:test+3])
print("z*1:", v1[test:test+3], "\nz*2:", v2[test:test+3])
#print("k_tr*z2-z0:", k_tr*(z2[test:test+3]-z0[test:test+3]))
print("z0:", z1[test:test+3], "\nz1:", z1[test:test+3], "\nz2:", z2[test:test+3])


plt.plot(np.arange(0,num),z0)
plt.plot(np.arange(0,num),a1)
plt.ylim(-.01, .01)
plt.xlim(0,num)
plt.show()