import numpy
import matplotlib.pyplot as plt


npoints = 420 # Number of sample points
dtheta = (numpy.pi - (-numpy.pi)) / float(npoints - 1)

thetas = numpy.zeros(npoints)
for i in range(npoints):
    thetas[i] = -numpy.pi + i * dtheta

f_sin = numpy.sin(thetas)
f_cos = numpy.cos(thetas)

ax = plt.plot(thetas, f_sin, label='sin', c='k', ls='--')
ax = plt.plot(thetas, f_cos, label='cos', color='r', linestyle='-.', linewidth=3.0)
_ = plt.xlabel('theta')
_ = plt.ylabel('function value')
_ = plt.xlim(-numpy.pi, numpy.pi)
_ = plt.legend()
_ = plt.savefig("sincos.pdf") # Save the plot to a PDF
