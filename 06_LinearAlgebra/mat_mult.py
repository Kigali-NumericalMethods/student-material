
import numpy

def mat_mult_mine(B, C):
    """
    Compute A = B * C using loops.
    Element wise this means a_ij = sum_k b_ik * c_kj.
    """
    if B.ndim != 2:
        raise ValueError('B must have dimension 2')
    if C.ndim != 2:
        raise ValueError('C must have dimension 2')

    nr_B, nc_B = B.shape[0], B.shape[1]
    nr_C, nc_C = C.shape[0], C.shape[1]

    if nc_B != nr_C:
        raise ValueError('Shape of B is not compatible with C. Cannot perform B * C.')

    # Allocate empty matrix of correct size to store A
    A = numpy.zeros((nr_B, nc_C))

    for i in range(nr_B): # loop over rows of C
        for j in range(nc_C): # loop over cols of C
            # COMPLETE CODE HERE
            # COMPLETE CODE HERE
            # COMPLETE CODE HERE
            # COMPLETE CODE HERE
            # COMPLETE CODE HERE
            # COMPLETE CODE HERE


    return A


B = numpy.array( [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]] )
C = numpy.array( [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]] )

# Call your code
A = mat_mult_mine(B, C)
print("A", A)

# Call the numpy equivalent of mat_vec()
A_ref = numpy.matmul(B, C)

# Compute the maximum difference between your result and the numpy result
diff = numpy.max(numpy.max(numpy.absolute(A_ref - A)))
print("difference =", ("%+1.12e")%diff)
