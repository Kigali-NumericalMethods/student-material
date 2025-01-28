
#
# Example of how to sort data using numpy.argsort
#

import numpy

# Create unsorted data for x
x = numpy.array([ 2.2, -0.1, 3.3, 1.1, 7.0])

# Create nicely ordered data for f (just to show how the sorting is applied)
f = numpy.array([ 0.0,  1.0, 2.0, 3.0, 4.0])


# argsort() looks at x and returns a set of indices which can 
# be used to re-order x from smallest value to largest value
# argsort() does NOT sort x for you - x remains untouched

idx = numpy.argsort(x)

# Create empty arrays to stored sorted and reordered data
x_sorted  = numpy.zeros(x.shape)
f_reorder = numpy.zeros(x.shape)

# Apply idx to reorder x so that its ordered frmo smallest to largest (e.g. sorted)

for i in range(x.shape[0]):
  x_sorted[i] = x[ idx[i] ]
# The loop above can be done in one line using x_sorted = x[idx]


print('x', x)
print('x_sorted', x_sorted);

# Reorder f using idx
for i in range(x.shape[0]):
  f_reorder[i] = f[ idx[i] ]

print('f', f)
print('f_reorder', f_reorder);

