import pandas as pd

my_data_set = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(my_data_set)

print(myvar)

print(pd.__version__)

""" 
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2

2.2.2
"""
