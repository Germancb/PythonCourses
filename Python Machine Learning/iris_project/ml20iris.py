from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt

# Load sample data
iris = load_iris()
features = iris.feature_names
X, y = iris.data, iris.target
print(iris.feature_names)
print(iris.target_names)
print(iris.data)
print(iris.target)
import pandas as pd
data = pd.DataFrame(iris.data, columns=iris.feature_names)
# Add the target as a new column
data['species'] = iris.target

# Calculate the correlation matrix
correlation_matrix = data.corr(numeric_only=True)
# Print the matrix
print(correlation_matrix)
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Decision Tree Classifier
dtree = DecisionTreeClassifier(criterion='entropy', max_depth=3)
# Train the model
dtree.fit(X_train, y_train)
tree.plot_tree(dtree, feature_names=features) 
plt.show()

# Make predictions
y_pred = dtree.predict(X_test)

# Evaluate the model (e.g., accuracy score)
from sklearn.metrics import accuracy_score
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")