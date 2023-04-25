from qutip.qip.operations import hadamard_transform
from qutip import Qobj,basis,Bloch,identity,sigmax,sigmay,sigmaz
import numpy as np
import scipy
import matplotlib.colors
import scipy

#the gate
# hadamard = hadamard_transform()
# the hamilton operator describing the evolution during the hadamard gate
# hamilton = Qobj(scipy.linalg.logm(hadamard.data.todense()), dims=hadamard.dims) / np.pi * 1.j

#create initial state vector
# psi0 = (basis(2, 0)).unit()

# describing the gate as time evolution
# def gate(t):
#     return (-2*np.pi*1.j*hamilton*t).expm()

# hadamard gate for t = 0.5
# In[1]: gate(0.5)
# Out[3]:
# Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
# Qobj data =
# [[ 0.70710678  0.70710678]
#  [ 0.70710678 -0.70710678]]

# evolve the gate
# n = 25
# psi = [gate(t)*psi0 for t in np.linspace(0, 1., 2*n)]

# plotting the states. State evolution during the first hamadard gate is red. During second hadamard gate is blue
# b = Bloch()
# b.vector_color = [matplotlib.colors.to_rgba('r', alpha=i) for i in np.arange(n)/float(n)] + [matplotlib.colors.to_rgba('b', alpha=i) for i in np.arange(n)/float(n)]  + ['black']
# b.add_states(psi)
# b.add_states([(basis(2,0) + (basis(2,0) + basis(2,1)).unit()).unit()])
#
# b.show()
# print("aaa")

# HW Code
p=0.2
phi=np.pi/2
theta = np.pi/4*0.8
psi0 = (Qobj(np.array([[np.cos(theta)**2],[np.exp(1j*phi)*np.sin(theta)**2]]))).unit()
psi0 = psi0*psi0.dag()

## problem 1
E0 = Qobj(np.array([[1,0],[0,np.sqrt(1-p)]]))
E1 = Qobj(np.array([[0,np.sqrt(p)],[0,0]]))

def evolve_amplitude_damping(state):
    newstate= E0*state*E0.dag()+E1*state*E1.dag()
    return newstate

n=20
b = Bloch()
b.add_states(psi0)
psi=psi0
for i in range(n):
    psi = evolve_amplitude_damping(psi)
    b.add_states(psi)
b.show()
b.clear()

# problem 2
p=0.2
phi=np.pi/2
theta = np.pi/4*0.8
psi0 = (Qobj(np.array([[np.cos(theta)**2],[np.exp(1j*phi)*np.sin(theta)**2]]))).unit()
psi0 = psi0*psi0.dag()
E0 = Qobj(np.array([[1,0],[0,np.sqrt(1-p)]]))
E1 = Qobj(np.array([[0,0],[0,np.sqrt(p)]]))

def evolve_phase_damping(state):
    newstate= E0*state*E0.dag()+E1*state*E1.dag()
    return newstate

n=20
b.add_states(psi0)
psi=psi0
for i in range(n):
    psi = evolve_phase_damping(psi)
    b.add_states(psi)
b.show()
b.clear()

## problem 3
p=0.2
phi=np.pi/2*1.5
theta = np.pi/4*0.8
psi0 = (Qobj(np.array([[np.cos(theta)**2],[np.exp(1j*phi)*np.sin(theta)**2]]))).unit()
psi0 = psi0*psi0.dag()

def evolve_depolarizing(state):
    newstate= p/2*identity(2) + (1-p)*state
    return newstate

n=100
b.add_states(psi0)
psi=psi0
for i in range(n):
    psi = evolve_depolarizing(psi)
    rx = (psi * sigmax()).tr()
    ry = (psi * sigmay()).tr()
    rz = (psi * sigmaz()).tr()
    b.add_points([rx,ry,rz])
b.show()