import numpy as np
from cmath import sqrt
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 1000)  # create an array of 1000 equally spaced values from -4 to 4
# x2 =np.concatenate([np.linspace(-10, -4, 1000), np.linspace(4, 10, 1000)])
x2 =np.linspace(0, 10, 1000)
# define the function y
def y(x):
    return 1/4*(-3*x+np.sqrt(-16+x**2+0j))

# plot the real part of y
plt.plot(x2, y(x2).real, label='Real('+ r'$\lambda_4$' +')')

# plot the imaginary part of y
plt.plot(x, y(x).imag, label='Imaginary('+ r'$\lambda_4$' +')')

plt.legend()
plt.xlabel(r'$\gamma$')
plt.ylabel(r'$\lambda_4$')
plt.show()