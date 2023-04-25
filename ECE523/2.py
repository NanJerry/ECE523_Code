import numpy as np
sx = np.array([[0, 1],  [ 1, 0]], dtype=np.complex128)
sy = np.array([[0, -1j],[1j, 0]], dtype=np.complex128)
sz = np.array([[1, 0],  [0, -1]], dtype=np.complex128)
id = np.array([[1, 0],  [ 0, 1]], dtype=np.complex128)

x_y = np.kron(sx,sy)
x_z = np