import pandas as pd

# What is a DataFrame?
""" A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns. """

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
#  calories  duration
# 0       420        50
# 1       380        40
# 2       390        45


#       Locate Row
""" As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s) """

# Note: This example returns a Pandas Series.
print(df.loc[2])
# calories    390
# duration     45
# Name: 2, dtype: int64


# Return row 0 and 1:
# use a list of indexes:
print(df.loc[[0, 1]])
"""  calories  duration
0       420        50
1       380        40 """
# Note: When using [], the result is a Pandas DataFrame


# CREATING OUR OWN INDEXES
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
"""      calories  duration
day1       420        50
day2       380        40
day3       390        45 """
print(df.loc["day2"])


# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.
""" df = pd.read_csv('data.csv')

print(df)  """ 
