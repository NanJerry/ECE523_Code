from qutip import tensor, sigmax, sigmay, identity, bell_state, bra, Qobj
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

## construct bell basis matrix
bellBasisBack=Qobj()
for i in range(4):
    bell=bell_state(np.binary_repr(i,2))
    anci= bra(np.binary_repr(i,2))
    bellBasisBack = bellBasisBack + tensor(anci, bell)
bellBasis=Qobj(bellBasisBack.inv().full())
bellBasisBack=Qobj(bellBasisBack.full())
## X
x = sp.symbols("x")

Noice = (sigmax() + sigmay()) / np.sqrt(2)
Hamil = tensor(sigmax(), sigmay()) + tensor(identity(2), Noice) + tensor(Noice, identity(2))
values, states = Hamil.eigenstates()

matrices=[]
dim = len(values)
for i in range(dim):
    matrices.append(Qobj((states[i] * states[i].dag()).full()))

def getEvolMatrix(t):
    a = Qobj(np.zeros([4, 4]))
    for i in range(dim):
        a = a + np.exp(-1j * values[i] * t) * matrices[i]
    return a

def projection(state,remainStatis):
    # projection matrox
    projMatr=np.zeros([4,4])
    projMatr[0,0]=1
    projMatr[1,1]=1
    projMatr=Qobj(projMatr)
    curstate=projMatr*state
    keepStatis=np.sqrt(np.abs(curstate[0][0])**2+np.abs(curstate[1][0])**2)[0]
    curstate=curstate/keepStatis
    statis=remainStatis*keepStatis
    return statis,curstate

sampleNum=1200
time=np.linspace(0,1.5,sampleNum)
measure_times=5 ## adjust time
measure_period=0
if (measure_times==0):
    measure_period=sampleNum+1
else:
    measure_period=np.ceil(sampleNum/measure_times)
# measure_period=168
measure_period_time=1.5/sampleNum*measure_period
Phi_P=[]
Phi_M=[]
Psi_P=[]
Psi_M=[]
t1=t2=t3=t4=0
remainStatis=[1]
theState= Qobj(bell_state().full())
evolMatrix=getEvolMatrix(time[1])
for i in range(sampleNum):
    theState = evolMatrix * theState
    curBellState = bellBasis * theState
    if (i!=0):
        if ((i%measure_period) == 0):
            newStat,curBellState=projection(curBellState,remainStatis[i-1])
            theState=bellBasisBack*curBellState
            remainStatis.append(newStat)
        else:
            remainStatis.append(remainStatis[i-1])
    curBellState=curBellState.full()
    curBellState.resize(4)
    Phi_P.append(np.abs(curBellState[0])**2)
    Phi_M.append(np.abs(curBellState[1])**2)
    Psi_P.append(np.abs(curBellState[2])**2)
    Psi_M.append(np.abs(curBellState[3])**2)


    if t1==0 and np.abs(np.abs(curBellState[0])**2-np.cos(time[i])**2) > 0.01:
        t1=time[i]
    if t2==0 and np.abs(np.abs(curBellState[1])**2-np.sin(time[i])**2) > 0.01:
        t2=time[i]

plt.plot(time, Phi_P, label = "Phi_P")
plt.plot(time, Phi_M, label = "Phi_M")
plt.plot(time, Psi_P, label = "Psi_P")
plt.plot(time, Psi_M, label = "Psi_M")
plt.legend()
plt.show()

plt.plot(time, remainStatis, label="Remaining Statis")
plt.legend()
plt.show()