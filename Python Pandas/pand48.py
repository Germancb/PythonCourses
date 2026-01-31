import pandas as pd

with pd.ExcelFile("data2a.xlsx") as xls:
    print(xls.sheet_names)

