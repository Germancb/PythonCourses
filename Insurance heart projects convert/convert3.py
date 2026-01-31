import pandas as pd
df = pd.read_csv('insurance.csv')
# Example: converting smoker to numeric
df['smoker_numeric'] = df['smoker'].map({'yes': 1, 'no': 0})
print(df)
#This creates a new column smoker_numeric with values:
#•	1 for smoker
# •	0 for non-smoker
#  Then You Can Do Correlation:
correlation = df[['smoker_numeric', 'charges']].corr()
print(correlation)

