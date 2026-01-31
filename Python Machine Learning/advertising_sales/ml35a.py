import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
dataset = pd.read_csv('advertising_sales.csv')

# Ensure correct feature selection: selecting columns for features (X) and target (y)
X = dataset.iloc[:, 1:4]  # Features (assuming columns 1 to 3 are the features)
y = dataset['Sales']      # Target (Sales)

# Split dataset into training and testing sets (80% train, 20% test, for example)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the linear regression model
lin = LinearRegression()

# Fit the model on the training data
lin.fit(X_train, y_train)

# Predict using the trained model
y_pred = lin.predict(X_test)

# Output predictions and model coefficients
print("Predictions:", y_pred)
print("Coefficients:", lin.coef_)
print("Intercept:", lin.intercept_)