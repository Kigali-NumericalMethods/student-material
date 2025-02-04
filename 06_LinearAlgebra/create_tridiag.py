
import numpy
import scipy.linalg as scl
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix

def create_mat(val0, val1, n):
  """
  Create a tri-diagonal matrix.

  Input:
    val0: float
      Value to the main diagonal (a_{ii} = val0)
    val1: float
      Value on the subdiagonal/(lower & upper) diagonal,
      i.e. the first diagonal below the main diagonal.
      a_{ij} = val1 = a_{ji} for j = i + 1

  Output:
    A: numpy.ndarray, shape = (n,n)
      Tri-diagonal matrix
  """

  if n < 2:
    raise ValueError("`n` must be greater than 1")

  row = numpy.zeros(n)
  row[0] = val0
  row[1] = val1

  A = scl.toeplitz(row, row)
  return A


def create_triangular_mat(val0, val1, n, lower=False):
  """
  Default is to create values in the upper triangular part of the matrix.
  If you want the lower triagular part only, set `lower = True`.
  """

  if n < 2:
    raise ValueError("`n` must be greater than 1")

  values = numpy.zeros(n)
  values[0] = val0
  values[1] = val1

  identity = numpy.zeros(n)
  identity[0] = val0

  if lower == False:
    A = scl.toeplitz(identity, values)
  else:
    A = scl.toeplitz(values, identity)

  return A

def create_sparse_mat(val0, val1, n):
  """
  Create a sparse tri-diagonal matrix.

  Input:
    val0: float
      Value to the main diagonal (a_{ii} = val0)
    val1: float
      Value on the subdiagonal/(lower & upper) diagonal,
      i.e. the first diagonal below the main diagonal.
      a_{ij} = val1 = a_{ji} for j = i + 1

  Output:
    B: numpy.csr, shape = (n,n)
      Tri-diagonal matrix
  """

  if n < 2:
    raise ValueError("`n` must be greater than 1")


  # Stencil
  row_idx = list()
  col_idx = list()
  for i in range(n):
    if i == 0:
      row_idx.append(i)
      col_idx.append(i)
      row_idx.append(i)
      col_idx.append(i+1)
    elif i == n-1:
      row_idx.append(i)
      col_idx.append(i)
      row_idx.append(i)
      col_idx.append(i-1)
    else:
      row_idx.append(i)
      col_idx.append(i+1)
      row_idx.append(i)
      col_idx.append(i)
      row_idx.append(i)
      col_idx.append(i-1)
  N = len(row_idx)
  z = numpy.zeros(N)

  A = coo_matrix((z, (row_idx, col_idx)), shape=(n, n))
  B = A.tocsr()

  # Fill Stencil
  for i in range(n):
    if i == 0:
      row_idx = i
      col_idx = i
      B[row_idx, col_idx] = val0

      row_idx = i
      col_idx = i+1
      B[row_idx, col_idx] = val1
    elif i == n-1:
      row_idx = i
      col_idx = i
      B[row_idx, col_idx] = val0

      row_idx = i
      col_idx = i-1
      B[row_idx, col_idx] = val1
    else:
      row_idx = i
      col_idx = i+1
      B[row_idx, col_idx] = val1

      row_idx = i
      col_idx = i
      B[row_idx, col_idx] = val0

      row_idx = i
      col_idx = i-1
      B[row_idx, col_idx] = val1

  return B
