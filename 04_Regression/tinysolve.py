#
# Taken from
# https://stackoverflow.com/questions/8690456/numerically-stable-inverse-of-a-2x2-matrix
#

import numpy as np

def solve2x2(A, rhs):
    """
    Stable solve of a 2x2 matrix.
    If the matrix is singular, x will be returned filled with NaN's

    Input:
      A: numpy.ndarray, shape = (2,2)
        Matrix.
      rhs: numpy.ndarray, shape = (2,)
        Right hand side vector.
    Output:
      x: numpy.ndarray, shape = (2,)
        Solution vector.
    """

    if A.ndim != 2: raise ValueError("Dim must be 2")
    if A.shape[0] != 2: raise ValueError("nrows must be 2")
    if A.shape[1] != 2: raise ValueError("ncols must be 2")
    x = np.zeros(rhs.shape)

    a, b, d, e = A[0,0], A[0, 1], A[1, 0], A[1, 1]
    c, f = rhs[0], rhs[1]

    if a == 0 and d == 0: # singular
        x[:] = np.nan
        return x

    if np.abs(a) >= np.abs(d):
        pass
    else:
        #swap( (a, b, c), (d, e, f) )
        t1, t2, t3 = a, b, c
        a, b, c = d, e, f
        d, e, f = t1, t2, t3

    alpha  = d / a
    beta = e - b * alpha
    if beta == 0: # singular
        x[:] = np.nan
        return x
    gamma = f - c * alpha
    x[1] = gamma / beta
    x[0] = (c - b * x[1]) / a

    return x
