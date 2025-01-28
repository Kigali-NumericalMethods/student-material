
# Example of computin z = c + y with loops

import numpy

x = numpy.array( [1.0, 2.0, 3.0, ])
y = numpy.array( [4.0, 5.0, 6.0, ])

# Get number of elements in the first dimension of x and y
# A better code would check the dimensions of x and y match
# e.g. check that x.ndim == y.ndim
m_x = x.shape[0]
m_y = y.shape[0]

# If sizes match, allocate z of correct size
if m_x == m_y:
    z = numpy.zeros(m_x) # could also do z = numpy.zeros(x.shape) or z = numpy.zeros(y.shape)
else:
    raise ValueError("Size of x and y do not match")

# Because we raised an error if the sizes do not match, if we get
# to this point in the code then it is safe to execute the loop
for i in range(m_x):
    z[i] = x[i] + y[i]
