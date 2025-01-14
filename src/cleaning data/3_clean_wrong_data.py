#      Data of Wrong Format
""" Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format. """


# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:

import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())



# Removing Rows
""" The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

Example
Remove rows with a NULL value in the "Date" column:
 """
df.dropna(subset=['Date'], inplace = True)