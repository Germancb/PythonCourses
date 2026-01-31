import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv('advertising_sales.csv')

# Check the first few rows and data structure
print(dataset.head())
print(dataset.info())

# Handle missing values (if necessary)
dataset.fillna(dataset.mean(), inplace=True)  # Fill missing values with the mean

# Ensure all columns are numeric
X = dataset.iloc[:, 1:4]  # Assuming columns 1 to 3 are the features
y = dataset['Sales']      # Target variable (Sales)

X = X.apply(pd.to_numeric, errors='coerce')
y = pd.to_numeric(y, errors='coerce')

# Check for missing values after conversion
print(X.isnull().sum())
print(y.isnull().sum())

# Drop rows with NaN values if there are any remaining
X = X.dropna()
y = y.dropna()

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the shapes of the split data
print(X_train.shape)
print(y_train.shape)

# Train the linear regression model
lin = LinearRegression()
lin.fit(X_train, y_train)

# Make predictions
y_pred = lin.predict(X_test)

# Print predictions and model coefficients
print("Predictions:", y_pred)
print("Coefficients:", lin.coef_)
print("Intercept:", lin.intercept_)

# Plot histograms of numerical columns to inspect the distribution
dataset.hist(bins=20, figsize=(10, 8))
plt.show()
