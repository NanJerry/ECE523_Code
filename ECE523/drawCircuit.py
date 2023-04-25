from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
import matplotlib.pyplot as plt

# # Spatial Parity
qr = QuantumRegister(2, 'ρ')
anc = QuantumRegister(1, 'control')
circ=QuantumCircuit(anc,qr,ClassicalRegister(1,"classical bit"))
circ.h(0)
# circ.cnot(2,1)
# circ.ccx(0,1,2)
# circ.cnot(2,1)
circ.cswap(0,1,2)
circ.h(0)
circ.measure([0],[0])
circ.draw('mpl',filename="./1.png")
plt.show()


# Depolarizing channel
# qr = QuantumRegister(2, 'q')
# anc = QuantumRegister(1, 'psi')
# circ=QuantumCircuit(qr,anc)
# circ.initialize([1,0],0)
# circ.initialize([1,0],1)
# circ.h([0,1])
# circ.cx(1,2)
# circ.cz(0,2)
# circ.draw("mpl",filename="./2.png")
# plt.show()
