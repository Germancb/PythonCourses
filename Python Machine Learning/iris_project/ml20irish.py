import pandas as pd
data = pd.read_csv("C:\\Users\\ACER\\PYTHON COURSES\\Python Machine Learning\iris_project\iris.csv")
data['Species_numeric'] = data['Species'].replace({
    'Iris-setosa': 0,
    'Iris-versicolor': 1,
    'Iris-Virginica': 2
})
print(data[['Species', 'Species_numeric']].head())

# Compute correlation matrix for the whole DataFrame
correlation_matrix = data.corr(numeric_only=True)

# Display the correlation matrix
print(correlation_matrix)





