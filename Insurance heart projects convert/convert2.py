import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'education': ['Bachelors', 'Masters', 'PhD', 'Bachelors']})

# Define a mapping dictionary
education_mapping = {'Bachelors': 0, 'Masters': 1, 'PhD': 2}

# Apply the mapping
df['education_numeric'] = df['education'].replace(education_mapping)

print(df)

