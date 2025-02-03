
import numpy

def mat_vec_mine(A, x):
    """
    Compute y = A * x using loops.
    Element wise this means y_i = sum_k a_ik * x_k.
    """
    if A.ndim != 2:
        raise ValueError('A must have dimension 2')
    if x.ndim != 1:
        raise ValueError('x must have dimension 1')

    nr_A, nc_A = A.shape[0], A.shape[1]
    n_x = x.shape[0]
    if n_x != nc_A:
        raise ValueError('Shape of A is not compatible with x. Cannot perform A * x.')

    # Allocate empty vector of correct size to store y
    y = numpy.zeros(nr_A)

    for i in range(nr_A): # loop over rows of y
        # COMPLETE CODE HERE
        # COMPLETE CODE HERE
        # COMPLETE CODE HERE
        # COMPLETE CODE HERE
        # COMPLETE CODE HERE
        # COMPLETE CODE HERE

    return y


A = numpy.array( [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]] )
x = numpy.array( [1.1, 2.2, 3.3] )

# Call your code
y = mat_vec_mine(A, x)
print("y", y)

# Call the numpy equivalent of mat_vec()
y_ref = numpy.matmul(A, x)

# Compute the maximum difference between your result and the numpy result
diff = numpy.max(numpy.absolute(y_ref - y))
print("difference =", ("%+1.12e")%diff)
