"""Implementation of Kitzes (2013) in Python with NumPy and Pandas.

Kitzes, Justin. 2013.
‘An Introduction to Environmentally-Extended Input-Output Analysis’.
Resources 2 (4): 489–503. https://doi.org/10.3390/resources2040489.
    
"""

import numpy as np
import pandas as pd

# Sector names
T_idx = ['Agriculture','Manufacturing']

# =============================================================================
# IO basics
# =============================================================================

# Transaction matrix
T = np.array([
    [8, 5],
    [4, 2]
    ])

# Total output
x_out = np.array(
    [16,12]
    )

# Satellite accounts
q = np.array(
    [8,4]
    )

# Final demand
y = np.array(
    [3,6]
    )

# Identity matrix
I = np.identity(len(T))

# Technical coefficients
A = np.divide(T,x_out)

# Direct externalities
f = np.diag(
    np.divide(q,x_out)
    )

# =============================================================================
# Leontief inverse-based calculation approach
# =============================================================================

# Leontief inverse
L_linverse = np.linalg.inv(I - A) 


from scipy.linalg import lu
test = lu((I-A))

# Total intensities
F_linverse = np.dot(f,L_linverse)

# Scale to final demand
E_linverse = np.multiply(F_linverse,y)

# Turn NumPy Array into Pandas DataFrame with indexed rows and columns
E_linverse = pd.DataFrame(
    E_linverse,
    index = T_idx,
    columns = T_idx
    )

print('\n>>> Leontief inverse-based results:')
print('\nProduction-based-inventory:')
print(E_linverse.sum(axis=1)) # Rows/Outputs
print('\nConsumption-based-inventory:')
print(E_linverse.sum(axis=0)) # Columns/Inputs

# =============================================================================
# Series expansion-based calculation approach (approximation)
# =============================================================================

# Total intensities (first X production layers)
L_decomposed = {
    'Zeroth production layer'  : I,
    'First production layer'   : np.linalg.matrix_power(A, 1),
    'Second production layer'  : np.linalg.matrix_power(A, 2),
    'Third production layer'   : np.linalg.matrix_power(A, 3),
    'Fourth production layer'  : np.linalg.matrix_power(A, 4),
    'Fifth production layer'   : np.linalg.matrix_power(A, 5),
    'Sixth production layer'   : np.linalg.matrix_power(A, 6),
    'Seventh production layer' : np.linalg.matrix_power(A, 7),
    'Eight production layer'   : np.linalg.matrix_power(A, 8),
    'Ninth production layer'   : np.linalg.matrix_power(A, 9),
    'Tenth production layer'   : np.linalg.matrix_power(A,10),
    }

# sum(L_decomposed.values()) ≈ np.linalg.inv(I - A) 

# Leontief inverse
L_series = sum(L_decomposed.values())

# Total intensities
F_series = np.dot(f,L_series)

# Scale to final demand
E_series = np.multiply(F_series,y)

# Turn NumPy Array into Pandas DataFrame with indexed rows and columns
E_series = pd.DataFrame(
    E_series,
    index = T_idx,
    columns = T_idx
    )

print('\n>>> Series expansion-based results:')
print('\nProduction-based-inventory:')
print(E_series.sum(axis=1)) # Rows/Outputs
print('\nConsumption-based-inventory:')
print(E_series.sum(axis=0)) # Columns/Inputs