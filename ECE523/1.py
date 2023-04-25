from qiskit.quantum_info import Statevector,DensityMatrix,SparsePauliOp
import numpy as np
import sympy as sp
import math
# def HS(M1, M2):
#     """Hilbert-Schmidt-Product of two matrices M1, M2"""
#     return (np.dot(M1.conjugate().transpose(), M2)).trace()
#
# def c2s(c):
#     """Return a string representation of a complex number c"""
#     if c == 0.0:
#         return "0"
#     if c.imag == 0:
#         return "%g" % c.real
#     elif c.real == 0:
#         return "%gj" % c.imag
#     else:
#         return "%g+%gj" % (c.real, c.imag)
#
# def decompose(H):
#     """Decompose Hermitian 2^nx2^n matrix H into Pauli matrices"""
#     n = H.shape[0]
#     sx = np.array([[0, 1],  [ 1, 0]], dtype=np.complex128)
#     sy = np.array([[0, -1j],[1j, 0]], dtype=np.complex128)
#     sz = np.array([[1, 0],  [0, -1]], dtype=np.complex128)
#     id = np.array([[1, 0],  [ 0, 1]], dtype=np.complex128)
#     single_S = [id, sx, sy, sz]
#     single_labels = ['I', '\sigma_x', '\sigma_y', '\sigma_z']
#     S = []
#     labels = []
#     for i in range(n):
#         for j in range(n):
#
#
#     for i in range(4):
#         for j in range(4):
#             label = labels[i] + ' \otimes ' + labels[j]
#             a_ij = 0.25 * HS(np.kron(S[i], S[j]), H)
#             if a_ij != 0.0:
#                 print("%s\t*\t( %s )" % (c2s(a_ij), label))
def toLatex(A):
    paulis = A.paulis
    coeffs = A.coeffs
    # for i in range(coeffs.size):
    #     print("({num.real:+0.04f} {num.imag:+0.04f}j)".format(num=coeffs[i]) + paulis[i].to_label(), end="+")
    for i in range(coeffs.size):
        print("{num.real:+0.04f}".format(num=coeffs[i]) + paulis[i].to_label(), end="")
    print("")

JLP = np.diag([-15,-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15])/15
HO = np.zeros((16,16))
for i in range(15):
    HO[i,i+1] = math.sqrt(i+1)
    HO[i+1,i] = math.sqrt(i+1)
JLP_d = SparsePauliOp.from_operator(JLP)
HO_d = SparsePauliOp.from_operator(HO)
toLatex(JLP_d)
toLatex(HO_d)

def constructHO(n):
    HO = np.zeros((n,n))
    for i in range(n-1):
        HO[i, i + 1] = math.sqrt(i + 1)
        HO[i + 1, i] = math.sqrt(i + 1)
    return HO

HO_1 = SparsePauliOp.from_operator(constructHO(4))

print("2 " + str(HO_1.coeffs.size))
HO_2 = SparsePauliOp.from_operator(constructHO(8))
print("3 " + str(HO_2.coeffs.size))
print("4 " + str(HO_d.coeffs.size))
HO_3 = SparsePauliOp.from_operator(constructHO(32))
print("5 " + str(HO_3.coeffs.size))
HO_4 = SparsePauliOp.from_operator(constructHO(64))
print("6 " + str(HO_4.coeffs.size))
toLatex(HO_2)