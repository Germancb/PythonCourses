import pandas as pd  #hearth1.py   # hearth desease analysis
import numpy as np
import matplotlib.pyplot as plt  # %matplotlib inline
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay 
heart_df = pd.read_csv('heart.csv')
print(heart_df.head())
print(heart_df.info())
print(heart_df.describe())
categorical_cols = ["Sex", "ChestPainType", "FastingBS", "RestingECG", "ExerciseAngina", "ST_Slope", "HeartDisease"]
fig = plt.figure(figsize=(16,15))
# EDA
for idx, col in enumerate(categorical_cols):
    ax = plt.subplot(4, 2, idx+1)
    sns.countplot(x=heart_df[col], ax=ax)
    # add data labels to each bar
    for container in ax.containers:
        ax.bar_label(container, label_type="center")
        plt.show()  # 7
#  how these categorical variables relate to the presence of heart disease:
fig = plt.figure(figsize=(16,15))
for idx, col in enumerate(categorical_cols[:-1]):
    ax = plt.subplot(4, 2, idx+1)
    # group by HeartDisease
    sns.countplot(x=heart_df[col], hue=heart_df["HeartDisease"], ax=ax)
    # add data labels to each bar
    for container in ax.containers:
        ax.bar_label(container, label_type="center")
        plt.show()  # 6
    # Data cleaning
    heart_df[heart_df['RestingBP']==0].info()
    heart_df[heart_df['Cholesterol']==0].info()
    df_clean = heart_df.copy()
# Remove the record with RestingBP = 0
df_clean = df_clean[df_clean["RestingBP"] != 0]
# Create a mask for patients without heart disease
heartdisease_mask = df_clean["HeartDisease"]==0
# Get cholesterol values for patients with and without heart disease
cholesterol_without_heartdisease = df_clean.loc[heartdisease_mask, "Cholesterol"]
cholesterol_with_heartdisease = df_clean.loc[~heartdisease_mask, "Cholesterol"]
# Replace cholesterol = 0 values with the median for the respective group
df_clean.loc[heartdisease_mask, "Cholesterol"] = cholesterol_without_heartdisease.replace(to_replace = 0, value = cholesterol_without_heartdisease.median())
df_clean.loc[~heartdisease_mask, "Cholesterol"] = cholesterol_with_heartdisease.replace(to_replace = 0, value = cholesterol_with_heartdisease.median())
# Verify our cleaning worked
print(df_clean[["Cholesterol", "RestingBP"]].describe())
df_clean = pd.get_dummies(df_clean, drop_first=True)
print(df_clean.head())
correlations = abs(df_clean.corr())
plt.figure(figsize=(12,8))
sns.heatmap(correlations, annot=True, cmap="rocket_r")
plt.show()
plt.figure(figsize=(12,8))
sns.heatmap(correlations[correlations > 0.30], annot=True, cmap="rocket_r")
plt.show()
# Building a Single-Feature Classifier. # Split data into training and validations sets
X = df_clean.drop(["HeartDisease"], axis=1)
y = df_clean["HeartDisease"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.15, random_state=417)
features = [
    "MaxHR",
    "Oldpeak",
    "Sex_M",
    "ExerciseAngina_Y",
    "ST_Slope_Flat",
    "ST_Slope_Up"
]
for feature in features:
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train[[feature]], y_train)
    accuracy = knn.score(X_val[[feature]], y_val)
    print(f"The k-NN classifier trained on {feature} and with k = 3 has an accuracy of {accuracy*100:.2f}%")
#[5 rows x 16 columns]
#The k-NN classifier trained on MaxHR and with k = 3 has an accuracy of 55.07%
#The k-NN classifier trained on Oldpeak and with k = 3 has an accuracy of 58.70%
#The k-NN classifier trained on Sex_M and with k = 3 has an accuracy of 61.59%
#The k-NN classifier trained on ExerciseAngina_Y and with k = 3 has an accuracy of 73.19%
#The k-NN classifier trained on ST_Slope_Flat and with k = 3 has an accuracy of 81.88%
# The k-NN classifier trained on ST_Slope_Up and with k = 3 has an accuracy of 55.07%
# Building a Multi-Feature Classifier # Scale the features to the same range
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train[features])
X_val_scaled = scaler.transform(X_val[features])
# Build and evaluate the model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)
accuracy = knn.score(X_val_scaled, y_val)
print(f"Accuracy: {accuracy*100:.2f}")   # Accuracy  Accuracy: 83.33
#Hyperparameter Optimization. Prepare data for final model
X = df_clean.drop(["HeartDisease"], axis=1)
y = df_clean["HeartDisease"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=417)
features = [
    "Oldpeak",
    # "Sex_M",  # Testing whether this feature helps or hinders accuracy
    "ExerciseAngina_Y",
    "ST_Slope_Flat",
    "ST_Slope_Up"
]
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train[features])
# Define hyperparameter grid
grid_params = {"n_neighbors": range(1, 20),
               "metric": ["minkowski", "manhattan"]}
# Perform grid search
knn = KNeighborsClassifier()
knn_grid = GridSearchCV(knn, grid_params, scoring='accuracy')
knn_grid.fit(X_train_scaled, y_train)
# Display best parameters
print(f"Best score: {knn_grid.best_score_*100:.2f}%")   # Best score: 82.16%
print(f"Best parameters: {knn_grid.best_params_}") # Bst score 82.29 Best parameters: {'metric': 'minkowski', 'n_neighbors': 11}
# Model Evaluation on Test Set. #Scale test data
X_test_scaled = scaler.transform(X_test[features])
# Make predictions on test set
predictions = knn_grid.best_estimator_.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy on test set: {accuracy*100:.2f}%")  # Model accuracy on test set 85.51%
# heck if there's any significant difference in the distribution of our data between the training and test sets:
# Check distribution of Sex_M # Check distribution of sex_M
print("Distribution of patients by their sex in the entire dataset")
print(X.Sex_M.value_counts())
print("\nDistribution of patients by their sex in the training dataset")
print(X_train.Sex_M.value_counts())
print("\nDistribution of patients by their sex in the test dataset")
print(X_test.Sex_M.value_counts())
# visualize the model's performance using a confusion matrix:
cf = confusion_matrix(y_test, predictions)
ConfusionMatrixDisplay(cf).plot()
plt.show()