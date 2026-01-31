import pandas as pd
pd.options.display.max_rows=1000
df=pd.read_csv('ventas.csv', index_col=0)
print(df)