"""Implementation of Kitzes (2013) in Python with NumPy and Pandas.

Kitzes, Justin. 2013.
‘An Introduction to Environmentally-Extended Input-Output Analysis’.
Resources 2 (4): 489–503. https://doi.org/10.3390/resources2040489.
    
"""

import numpy as np
import pandas as pd

# Sectors
T_idx = ['Agriculture','Manufacturing']

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
L = np.linalg.inv(I - A) 

# Total intensities
F = np.dot(f,L)

# Scale to final demand
E = np.multiply(F,y)

# Turn NumPy Array into Pandas DataFrame with indexed rows and columns
E = pd.DataFrame(
    E,
    index = T_idx,
    columns = T_idx
    )

# Production-based inventory
E_production_based = (
    E.sum(axis=1) # Rows/Outputs/Production
    )

# Consumption-based inventory
E_consumption_based = (
    E.sum(axis=0) # Columns/Inputs/Consumption
    )

print('\n>>> Leontief inverse-based results:')
print('\nProduction-based-inventory:')
print(E_production_based)
print('\nConsumption-based-inventory:')
print(E_consumption_based)

# =============================================================================
# Series expansion-based calculation approach (approximation)
# =============================================================================

# Total intensities (first eleven production layers)
F_Series = {
    'Zeroth production layer' : I,
    'First production layer' : np.linalg.matrix_power(A,1),
    'Second production layer' : np.linalg.matrix_power(A,2),
    'Third production layer' : np.linalg.matrix_power(A,3),
    'Fourth production layer' : np.linalg.matrix_power(A,4),
    'Fifth production layer' : np.linalg.matrix_power(A,5),
    'Sixth production layer' : np.linalg.matrix_power(A,6),
    'Seventh production layer' : np.linalg.matrix_power(A,7),
    'Eight production layer' : np.linalg.matrix_power(A,8),
    'Ninth production layer' : np.linalg.matrix_power(A,9),
    'Tenth production layer' : np.linalg.matrix_power(A,10),
    }

# sum(F_Series.values()) is an approxiamtion of L 
# Multiplication with f returns F
F = np.dot(f,sum(F_Series.values()))

# Scale to final demand
E = np.multiply(F,y)

# Turn NumPy Array into Pandas DataFrame with indexed rows and columns
E = pd.DataFrame(
    E,
    index = T_idx,
    columns = T_idx
    )

# Production-based inventory
E_production_based = (
    E.sum(axis=1) # Rows/Outputs/Production
    )

# Consumption-based inventory
E_consumption_based = (
    E.sum(axis=0) # Columns/Inputs/Consumption
    )

print('\n>>> Series expansion-based results:')
print('\nProduction-based-inventory:')
print(E_production_based)
print('\nConsumption-based-inventory:')
print(E_consumption_based)