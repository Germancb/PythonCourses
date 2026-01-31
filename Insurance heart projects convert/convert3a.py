import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')
# Example: converting smoker to numeric
df['smoker_numeric'] = df['smoker'].map({'yes': 1, 'no': 0})
print(df)
#This creates a new column smoker_numeric with values:
#•	1 for smoker   . 0 for non-smoker
#  Then You Can Do Correlation:
correlation = df[['smoker_numeric', 'charges']].corr()
print(correlation)   # include only charges and smoker.numeric

num_df = df.select_dtypes(include='number')  # Select only numeric columns  (5) age bmi children charges smoker_numeric
# Now compute correlation
correlations = num_df.corr()
print(correlations)
sns.heatmap(correlations, cmap='Blues', annot=True)  # usa heatmap to visualize correlations (seaborn)
plt.show()

