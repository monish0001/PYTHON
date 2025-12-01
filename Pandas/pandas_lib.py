# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.


import pandas as pd
import numpy as np


data={
    "Name":["Monish","Karan","Ajay","Vijay","Kunal"],
    "Age":[25,31,45,23,12],
    "Address": ["Lko","Indore","Mumbai","Banglore","Hydrabad"] # all the list should be same size
}

df=pd.DataFrame(data)
print(df)


data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

