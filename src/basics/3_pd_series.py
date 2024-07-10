#    What is a Series?
""" A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type. """

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
# 0    1
# 1    7
# 2    2
# dtype: int64


#   Labels
""" If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value. """

print(myvar[0])  # 1


#   CREATING LABELS
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

print(myvar["y"])

""" 
x    1
y    7
z    2
dtype: int64
7
"""

#   KEY-VALUE PAIRS
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

""" 
day1    420
day2    380
day3    390
dtype: int64
"""


#     DataFrames

""" Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table. """

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)