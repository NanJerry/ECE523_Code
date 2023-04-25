import numpy as np

def gram_schmidt(A):
    (n, m) = A.shape

    for i in range(m):

        q = A[:, i]  # i-th column of A

        for j in range(i):
            q = q - np.vdot(A[:, j], A[:, i]) * A[:, j]

        if np.array_equal(q, np.zeros(q.shape)):
            raise np.linalg.LinAlgError("The column vectors are not linearly independent")

        # normalize q
        q = q / np.sqrt(np.vdot(q, q))

        # write the vector back in the matrix
        A[:, i] = q


Psi_1=np.array([1,0,0,-1j])/np.sqrt(2)
Psi_2=np.array([1,0,0,1])/np.sqrt(2)
Psi_3=np.array([0,1,-1,0])/np.sqrt(2)
Psi_4=np.array([1,1,1,1])/2

set1=np.vstack([Psi_1,Psi_2,Psi_3,Psi_4]).T
set2=np.vstack([Psi_4,Psi_1,Psi_2,Psi_3]).T
set3=np.vstack([Psi_3,Psi_4,Psi_1,Psi_2]).T
set4=np.vstack([Psi_2,Psi_3,Psi_4,Psi_1]).T

gram_schmidt(set1)
gram_schmidt(set2)
gram_schmidt(set3)
gram_schmidt(set4)