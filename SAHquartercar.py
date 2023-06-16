
import os, random
os.system('cls')
print("----------------------------------------\n      Quarter-Car Model Attempt 2:\n----------------------------------------")
import numpy as np
# from numpy import loadtxt
from matplotlib import pyplot as plt
np.set_printoptions(precision=2, sign='+', suppress=True, floatmode='fixed')

# Quality Factor - Stations per meter
QF = 6

# Road Length (meters)
RL = 300

ZR = np.zeros(QF*RL)
ZW = np.zeros(QF*RL)
ZB = np.zeros(QF*RL)

FKW = np.zeros(QF*RL)
FCW = np.zeros(QF*RL)
FKT = np.zeros(QF*RL)
FCT = np.zeros(QF*RL)

AB = np.zeros(QF*RL)
AU = np.zeros(QF*RL)

dZB = np.zeros(QF*RL)
dZW = np.zeros(QF*RL)
dZR = np.zeros(QF*RL)
dZS = np.zeros(QF*RL)
dZC = np.zeros(QF*RL)


kT = 180000
kW = 30000

mB = 454.5
mU = mB*0.1

zeta = 0.7
#c_sh = 2*np.sqrt(k_s*m_s) * zeta
CW = 2*np.sqrt(kW*mB) * zeta
CT = 2*np.sqrt(kT*mU) * 0.5

V = 100 / 3.6
dt = 1/(QF*V)

roadrange = 0.025/QF
testfreq = 1
testamp = 0.025/(testfreq**(1/5))

for i in range(2,QF*RL):
    #ZR[i] = testamp/2*(-np.cos(2*testfreq*dt*i*np.pi) + 1)
    ZR[i] = ZR[i-1] + random.triangular(-roadrange - ZR[i-1]/2, roadrange - ZR[i-1]/2, 0)
    
    FKT[i] = kT*(ZR[i-1] - ZW[i-1])
    FKW[i] = kW*(ZW[i-1] - ZB[i-1])
    FCW[i] = CW*dZS[i-1]
    #FCT[i] = CT*dZS[i-1]
    
    AB[i] = (FKW[i] + FCW[i]) / mB
    AU[i] = (FKT[i] + FCT[i] - FKW[i] - FCW[i]) / mU
    
    dZB[i] = dZB[i-1] + AB[i]*dt
    ZB[i] = ZB[i-1] + dZB[i]*dt
    dZW[i] = dZW[i-1] + AU[i]*dt
    ZW[i] = ZW[i-1] + dZW[i]*dt
    
    dZS[i] = ((ZW[i] - ZB[i]) - (ZW[i-1] - ZB[i-1]))
    #dZC[i] = ((ZR[i] - ZW[i]) - (ZR[i-1] - ZW[i-1]))
    
    
    
    
#    dZR[i] = ZR[i] - ZR[i-1]
#print(ZR)
#print(CW)
print(np.max(AB))



plt.plot(np.arange(0, QF*RL)/QF, ZR)
plt.plot(np.arange(0, QF*RL)/QF, ZW)
plt.plot(np.arange(0, QF*RL)/QF, ZB)
#plt.plot(np.arange(0, QF*RL)/QF, ZW-ZB)
#plt.plot(np.arange(0, QF*RL)/QF, dZR)
#plt.plot(np.arange(0,QF*RL)/QF,a1)
plt.ylim(-10*roadrange, 10*roadrange)
plt.xlim(0,RL)
plt.xlabel("Road Travel (m)")
plt.ylabel("Height Change (m)")

plt.xticks(np.arange(0, RL, RL/10))

plt.show()

