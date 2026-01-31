import pandas as pd
df = pd.read_csv('insurance.csv')
# Example: converting smoker to numeric
# dfdf['smoker_numeric'] = df['smoker'].map({'yes': 1, 'no': 0})
df["is_smoker"] = (df["smoker"] == "yes")
print(df)
#This creates a new column is_smoker  with values Tre/False:
#  Then You Can Do Correlation:
correlation = df[['is_smoker', 'charges']].corr()
print(correlation)

