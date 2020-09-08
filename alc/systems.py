__all__ = [
  "solve"
]

from alc.gauss import gauss_elimination
from alc.utils import zeros
from alc.jacobi import jacobi
from alc.gauss_seidel import gauss_seidel

def solve (A, B, method='gauss_elimination', threshold=1e-3):
  if method == "gauss_elimination":
    # Turn A into an upper triangular matrix
    A, intermediates = gauss_elimination (A, return_intermediates=True, show_steps=False, return_pivots=False)
    # To keep it an equation, apply transformations to B as well
    for m in intermediates:
      B = m * B
    # Initialize x
    x = zeros((A.shape[0], B.shape[1]))
    n = A.shape[0]
    # Retro-substitution
    x[n-1] = [B[n-1][0]/A[n-1][n-1]]
    for i in range(n-2, -1, -1):
      x[i] = [B[i][0]/A[i][i]]
      for j in range(i+1, n):
        x[i][0] -= A[i][j]*x[j][0] / A[i][i]
    return x
  elif method == "jacobi":
    x = jacobi(A, B, threshold=threshold)
    return x
  elif method == "gauss_seidel":
    x = gauss_seidel(A, B, threshold=threshold)
    return x
  else:
    raise NameError("Solving method not allowed!")