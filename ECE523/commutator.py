import qutip as qp
import numpy as np
Set = []
Set.append(qp.identity(2))
Set.append(qp.sigmax())
Set.append(qp.sigmay())
Set.append(qp.sigmaz())
UniSet = []
Result=[]
Noiseless=qp.tensor(qp.sigmax(),qp.sigmay())
for i in range(4):
    for j in range(4):
        a=qp.Qobj(qp.commutator(qp.tensor(Set[i],Set[j]),Noiseless).full())
        if a == qp.Qobj(np.zeros((4,4))):
            UniSet.append((i,j))

