import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
dataset = pd.read_csv('advertising_sales.csv')

# Ensure correct feature selection: selecting columns for features (X) and target (y)
X = dataset.iloc[:, 1:4]  # Features (assuming columns 1 to 3 are the features)
y = dataset['Sales']      # Target (Sales)

# Convert to numeric if needed (to avoid issues with strings or non-numeric data)
X = X.apply(pd.to_numeric, errors='coerce')  # Apply pd.to_numeric on X to ensure all values are numeric
y = pd.to_numeric(y, errors='coerce')        # Ensure 'Sales' is numeric

# Check for missing values after conversion
print(X.isnull().sum())  # Check if there are any missing values in features
print(y.isnull().sum())  # Check if there are any missing values in target variable

# Drop any rows with NaN values (if necessary)
X = X.dropna()
y = y.dropna()

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check shapes of X_train and y_train
print(X_train.shape)
print(y_train.shape)

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

