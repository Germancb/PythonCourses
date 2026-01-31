import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'Category': ['A', 'B', 'A', 'C', 'B'],
            'Value': [10, 15, 12, 18, 14]}
df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['Category'], drop_first=True) # drop_first avoids multicollinearity
correlation_matrix = df_encoded.corr()
print(correlation_matrix)

le = LabelEncoder()
df['Category_encoded'] = le.fit_transform(df['Category'])

correlation_matrix = df[['Category_encoded', 'Value']].corr()
print(correlation_matrix)
