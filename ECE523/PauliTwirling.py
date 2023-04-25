from qutip import tensor, sigmax, sigmay, sigmaz,identity, bell_state, bra, Qobj
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random
from datetime import datetime
random.seed(datetime.now().timestamp())

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

twirling_set=[identity(4),Qobj(tensor(identity(2),sigmay()).full()), \
              Qobj(tensor(sigmax(),identity(2)).full()),\
              Qobj(tensor(sigmax(),sigmay()).full()),\
              Qobj(tensor(sigmay(),sigmax()).full()),\
              Qobj(tensor(sigmay(),sigmaz()).full()),\
              Qobj(tensor(sigmaz(),sigmax()).full()),\
              Qobj(tensor(sigmaz(),sigmaz()).full())]
# twirling_set=[Qobj(tensor(identity(2),sigmay()).full()), \
#               Qobj(tensor(sigmax(),identity(2)).full()),\
#               Qobj(tensor(sigmax(),sigmay()).full()),\
#               Qobj(tensor(sigmay(),sigmax()).full()),\
#               Qobj(tensor(sigmay(),sigmaz()).full()),\
#               Qobj(tensor(sigmaz(),sigmax()).full())]
twirling_size=len(twirling_set)
sampleNum=1650
time=np.linspace(0,1.5,sampleNum)
twirling_layers=55 ## adjust time
twirling_period=0
if (twirling_layers==0):
    twirling_period=sampleNum+1
else:
    twirling_period=np.ceil(sampleNum/twirling_layers)
# measure_period=168
twirling_period_time= 1.5 / sampleNum * twirling_period
Phi_P=[]
Phi_M=[]
Psi_P=[]
Psi_M=[]
t1=t2=t3=t4=0
theState= Qobj(bell_state().full())
evolMatrix=getEvolMatrix(time[1])
twirling_op=identity(4)
# twirling_Matrix=getEvolMatrix(twirling_period_time)
for i in range(sampleNum):
    # do twirl here
    if ((i%twirling_period) == 0):
        theState=twirling_op*theState
        choice=random.randrange(twirling_size)
        twirling_op=twirling_set[choice]
        theState = twirling_op * theState
    theState = evolMatrix * theState
    curBellState = bellBasis * twirling_op * theState
    if (i==(sampleNum-1)):
        theState=twirling_op*theState
        curBellState = bellBasis * theState

    curBellState=curBellState.full()
    curBellState.resize(4)
    Phi_P.append(np.abs(curBellState[0])**2)
    Phi_M.append(np.abs(curBellState[1])**2)
    Psi_P.append(np.abs(curBellState[2])**2)
    Psi_M.append(np.abs(curBellState[3])**2)

    if t1==0 and np.abs(np.abs(curBellState[0])**2-np.cos(time[i])**2) > 0.1:
        t1=time[i]
    if t2==0 and np.abs(np.abs(curBellState[1])**2-np.sin(time[i])**2) > 0.1:
        t2=time[i]

plt.plot(time, Phi_P, label = "Phi_P")
plt.plot(time, Phi_M, label = "Phi_M")
plt.plot(time, Psi_P, label = "Psi_P")
plt.plot(time, Psi_M, label = "Psi_M")
plt.legend()
plt.show()