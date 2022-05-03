# Readme

The file [`main.py`](main.py) contains a most simple implementation of [Kitzes (2013)](https://doi.org/10.3390/resources2040489) in Python with the packages [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/).

> Kitzes, Justin. 2013. ‘An Introduction to Environmentally-Extended Input-Output Analysis’. Resources 2 (4): 489–503. [https://doi.org/10.3390/resources2040489](https://doi.org/10.3390/resources2040489).

_Note: [Pymrio](https://github.com/konstantinstadler/pymrio) is a comprehensive package for Multi-Regional Input-Output Analysis (MRIO) in Python._

## Output of [`main.py`](main.py):

| Inventory           | Sector        | Leontief inverse-based results | Series expansion-based results[^1] |
|---------------------|---------------|--------------------------------|------------------------------------|
| Production-based    | Agriculture   | 8.00000                        | 7.826207                           |
| Production-based    | Manufacturing | 4.00000                        | 3.945339                           |
| Consumption-based   | Agriculture   | 4.80000                        | 4.711197                           |
| Consumption-based   | Manufacturing | 7.20000                        | 7.060348                           |

```Txt
>>> Leontief inverse-based results:

Production-based-inventory:
Agriculture      8.0
Manufacturing    4.0
dtype: float64

Consumption-based-inventory:
Agriculture      4.8
Manufacturing    7.2
dtype: float64

>>> Series expansion-based results:

Production-based-inventory:
Agriculture      7.826207
Manufacturing    3.945339
dtype: float64

Consumption-based-inventory:
Agriculture      4.711197
Manufacturing    7.060348
dtype: float64
```

[^1]: Calculated for the first eleven production layers (see [`main.py`](main.py)).