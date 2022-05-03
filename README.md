The file [`main.py`](main.py) contains a most simple implementation of [Kitzes (2013)](https://doi.org/10.3390/resources2040489) in Python with the packages [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/).

Kitzes, Justin. 2013. ‘An Introduction to Environmentally-Extended Input-Output Analysis’. Resources 2 (4): 489–503. [https://doi.org/10.3390/resources2040489](https://doi.org/10.3390/resources2040489).

Output of [`main.py`](main.py):
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

[Pymrio](https://github.com/konstantinstadler/pymrio) is a package for Multi-Regional Input-Output Analysis (MRIO) in Python.