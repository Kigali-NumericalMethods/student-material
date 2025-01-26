

try:
  import numpy as np
except:
  raise RuntimeError('Failed to import', 'numpy')

try:
  import matplotlib.pyplot as plt
except:
  raise RuntimeError('Failed to import', 'matplotlib')

try:
  import scipy as sp
except:
  raise RuntimeError('Failed to import', 'scipy')

try:
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
except:
  raise RuntimeError('Failed to import', 'mplot3d')




def numpy_ex1():
  _a = np.linspace(1.,12.,12)
  a = _a.view()
  a.shape = (4,3)

  u,s,vt = np.linalg.svd(a, full_matrices=False)
  print(u)


def matplotlib_ex1():
  # evenly sampled time at 200ms intervals
  t = np.arange(0., 5., 0.2)

  # red dashes, blue squares and green triangles

  plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

  plt.savefig('mplib_ex1.pdf')


def scipy_ex1():
  _a = np.linspace(1.,12.,12)
  a = _a.view()
  a.shape = (4,3)

  u,s,vt = sp.linalg.svd(a, full_matrices=False)
  print(u)


def mplot3d_ex1():
  gravity = lambda G, R, drho, h, z : (1.0e8 * G * 4.0 * np.pi * R**3.0 * drho) / (3.0 * (h**2 + z**2)) # Gravitational attraction.


  x = np.arange(-6.0, 6.0, 0.1) # Range of x values
  y = np.arange(-6.0, 6.0, 0.1) # Range of y values
  X, Y = np.meshgrid(x, y) # Make a meshgrid object

  # Define the other parameters
  z = 3.0
  G = 6.67e-11 # Grav. constant in Nm^2/kg^2 (SI)
  R = 2.0 # Radius in meters
  drho = 500.0 # Density contrast in kg/m^3

  h = np.sqrt(X**2 + Y**2) # Get the horizontal distance from ground zero for x, y
  # and make the g array
  g = gravity(G, R, drho, h, z) # Multipy by a million to get the units reasonable for the plots.


  fig = plt.figure(6, (8, 5)) # Make a figure object
  ax = fig.add_subplot(111, projection='3d') # Give it the powers of an Axes3D object
  surf = ax.plot_surface(X, Y, g, alpha=0.3)
  cset = ax.contour(X, Y, g,zdir='z', offset=1, cmap=cm.jet)
  cset = ax.contour(X, Y, g,zdir='x', offset=-7, cmap=cm.jet)
  cset = ax.contour(X, Y, g,zdir='y', offset=7, cmap=cm.jet)
  ax.set_xlabel('X') # and label the axes
  ax.set_ylabel('Y')
  ax.set_zlabel('Z');

  plt.savefig('mplot3d_ex1.pdf')
  plt.show()



def main():

  numpy_ex1()

  matplotlib_ex1()

  scipy_ex1()

  mplot3d_ex1()

if __name__ == '__main__':
  main()
