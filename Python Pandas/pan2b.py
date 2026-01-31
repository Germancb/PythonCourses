# Panda series like a column in a table   Use of index
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a, index=["x","y","z"])
print(myvar,"y")
print(myvar)
print(type(myvar))