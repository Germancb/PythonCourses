import os

print(os.path.exists("data2a.xlsx"))  # Should return True if the file is accessible

print(os.getcwd())
print(os.path.exists("data2a.xlsx"))

import pandas as pd

# df = pd.read_excel("data2a.xlsx", index_col=0, skiprows=1, sheet_name="data2")
df = pd.read_excel("data2a.xlsx")
print(df)
