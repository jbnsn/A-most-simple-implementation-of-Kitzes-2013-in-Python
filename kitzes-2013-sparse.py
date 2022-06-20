import numpy as np
import scipy.sparse
import scipy.sparse.linalg

# Transaction matrix
T = scipy.sparse.csr_matrix(
    np.array([
        [8, 5],
        [4, 2]
        ])
    )

# Total output
x_out = np.array(
        [16,12]
        )

# Technical coefficients
A = scipy.sparse.csr_matrix(T / x_out)

def getL(
    A, # Technical coefficient matrix
    logging = False,
    threshold = 1E-5 # 0.001 %
    ):
    """
    Approximate (I - A)^-1.
    
    This function is an alternative to the execution of np.linalg.inv(I - A).
    
    L = (I-A)^-1
    L = (I-A)^-1 ≈ I + A + AA + AAA + AAAA ... ≈ I + A + A^2 + A^3 + A^4 ...

    Parameters
    ----------
    A : Matrix (e.g. np.array or scipy.sparse.csr_matrix)
        Technical coefficient matrix.
    logging : Boolean, optional
        Print production layer sum to file. The default is False.

    Returns
    -------
    L : Matrix (e.g. np.array or scipy.sparse.csr_matrix)
        Leontief inverse. Approximation of (I - A)^-1.

    """
    
    # Zeroth production layer
    I = scipy.sparse.identity(
        A.shape[0],
        # format = 'csc'
        )
    
    L = I.copy()
    
    # First production layer
    layer = A.copy()
    
    # ... add the ensuing production layer until
    # L_i.sum() is less than 0.001% of L.sum()
    while layer.sum()/I.sum() > threshold:
    
        L += layer
        layer = layer @ A 
    
        if logging: print(f"Sum: {layer.sum()/L.sum()}")

    return L

L_getL = getL(A, threshold = 1E-5, logging = True).todense()

L_SciPy = scipy.sparse.linalg.inv(
    scipy.sparse.eye(*A.shape, format='csc') - A
    )

print(L_getL)
print(L_SciPy.todense())
