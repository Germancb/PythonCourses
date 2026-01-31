from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'color': ['red', 'blue', 'green', 'red', 'blue']})

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the categorical column
df['color_encoded'] = label_encoder.fit_transform(df['color'])

print(df)