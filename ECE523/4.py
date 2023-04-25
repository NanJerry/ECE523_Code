from qutip import tensor, sigmax, sigmay, identity, bell_state, bra, Qobj
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

## construct bell basis matrix
bellBasis=Qobj()
for i in range(4):
    bell=bell_state(np.binary_repr(i,2))
    anci= bra(np.binary_repr(i,2))
    bellBasis =bellBasis+tensor(anci,bell)
bellBasis=Qobj(bellBasis.inv().full())

## X
x = sp.symbols("x")

Noice = (sigmax() + sigmay()) / np.sqrt(2)
Hamil = tensor(sigmax(), sigmay()) + tensor(identity(2), Noice) + tensor(Noice, identity(2))
values, states = Hamil.eigenstates()

matrices=[]
dim = len(values)
for i in range(dim):
    matrices.append(Qobj((states[i] * states[i].dag()).full()))

def getStateVector(t):
    a=Qobj(np.zeros([4,4]))
    for i in range(dim):
        a=a+np.exp(-1j*values[i]*t) * matrices[i]
    curState=a * Qobj(bell_state().full())
    curState=bellBasis*curState
    return curState


sampleNum=1000
time=np.linspace(0,2,sampleNum)
Phi_P=[]
Phi_M=[]
Psi_P=[]
Psi_M=[]
t1=t2=t3=t4=0
for i in range(sampleNum):
    a=getStateVector(time[i]).full()
    a.resize(4)
    Phi_P.append(np.abs(a[0])**2)
    Phi_M.append(np.abs(a[1])**2)
    Psi_P.append(np.abs(a[2])**2)
    Psi_M.append(np.abs(a[3])**2)
    if t1==0 and np.abs(np.abs(a[0])**2-np.cos(time[i])**2) > 0.01:
        t1=time[i]
    if t2==0 and np.abs(np.abs(a[1])**2-np.sin(time[i])**2) > 0.01:
        t2=time[i]
    if t3==0 and np.abs(np.abs(a[2])**2) > 0.01:
        t3=time[i]
    if t4==0 and np.abs(np.abs(a[3])**2) > 0.01:
        t4=time[i]

plt.plot(time, Phi_P, label = "Phi_P")
plt.plot(time, Phi_M, label = "Phi_M")
plt.plot(time, Psi_P, label = "Psi_P")
plt.plot(time, Psi_M, label = "Psi_M")
plt.legend()
plt.show()