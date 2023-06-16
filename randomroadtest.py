
import os, random
os.system('cls')
print("----------------------------------------\n         Random Road Function:\n----------------------------------------")
import numpy as np
from numpy import loadtxt
from matplotlib import pyplot as plt

np.set_printoptions(precision=2, sign='+', suppress=True, floatmode='fixed')

A = np.zeros(100) - 0
x = np.arange(0,100)

print(x)

Z = 0.03 + A[0]
zmax = Z
zmin = -Z



for i in range(2,100):
    A[i] = A[i-1] + random.triangular(zmin,zmax,A[0])
    zmax = Z - A[i]/2
    zmin = -Z - A[i]/2

print(A)

plt.plot(x,A)
plt.ylim(-0.10, 0.10)
plt.xlim(0,100)
plt.show()

print("Done!")