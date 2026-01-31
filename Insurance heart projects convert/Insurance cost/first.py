import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the insurance dataset
insurance = pd.read_csv('insurance.csv')
insurance.head()
print(insurance.head())
# for line in insurance:
#    print(line)
print(insurance.info())
print(insurance.describe())
insurance.hist('charges')
plt.show()

insurance["log_charges"] = np.log2(insurance["charges"])
insurance.hist("log_charges")
plt.show()

num_insurance = insurance.select_dtypes(include='number')

# Now compute correlation
correlations = num_insurance.corr()
print(correlations)
sns.heatmap(correlations, cmap='Blues', annot=True)
plt.show()

insurance_numeric = num_insurance[['age', 'bmi', 'children', 'charges']]
sns.pairplot(insurance_numeric, kind='scatter', plot_kws={'alpha': 0.4})
plt.show()

insurance.boxplot(column=["log_charges"], by="sex")
plt.show()

insurance.boxplot(column=["log_charges"], by="smoker")
plt.show()

insurance.boxplot(column=["log_charges"], by="region")
plt.show()

insurance["is_smoker"] = (insurance["smoker"] == "yes")
X = insurance[["age", "bmi", "is_smoker"]]
y = insurance["log_charges"]
# print(X)
# print(y)

# 75% for training set, 25% for test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=42)
insurance_model = LinearRegression()
insurance_model.fit(X_train, y_train)  ## error
print(insurance_model.coef_)

# array([0.0508618 , 0.01563733, 2.23214787])
y_pred = insurance_model.predict(X_train)
train_mse = mean_squared_error(y_train, y_pred)
print(train_mse)

train_mse_orig_scale = np.exp(mean_squared_error(y_train, y_pred))
print(train_mse_orig_scale)

train_r2 = r2_score(y_train, y_pred)
print(train_r2)

# Create a DataFrame with predictions and actual values for easier plotting
plot_df = pd.DataFrame({
    'predictions': y_pred,
    'actual': y_train,
    'is_smoker': X_train['is_smoker'],
    'age': X_train['age'],
    'bmi': X_train['bmi'],
    'residuals': y_train - y_pred,
})

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='predictions', y='actual',
                data=plot_df, alpha=0.7)

plt.xlabel('Predicted log_charges')
plt.ylabel('Actual log_charges')

plt.show()

sns.scatterplot(x='predictions', y='residuals',
                data=plot_df, alpha=0.7)
plt.show()

cdf = pd.DataFrame(insurance_model.coef_, X.columns, columns=['Coef'])
print(cdf)
print(insurance_model.intercept_)

test_pred = insurance_model.predict(X_test)
print(mean_squared_error(y_test, test_pred))

print(np.exp2(mean_squared_error(y_test, test_pred)))  #1.368815646563475

smokers_df = insurance[insurance["is_smoker"] == True]
X = smokers_df[["age", "bmi"]]
y = smokers_df["log_charges"]

# 75% for training set, 25% for test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=42)

smoker_model = LinearRegression()
smoker_model.fit(X_train, y_train)
print(smoker_model.coef_)  #[0.01282851 0.07098738]

y_pred = smoker_model.predict(X_train)
train_mse = mean_squared_error(y_train, y_pred)
print(train_mse)   # 0.07046354357369701

train_r2 = r2_score(y_train, y_pred)
print(train_r2) # 0.7661650418251629

# Create a DataFrame with predictions and actual values for easier plotting
plot_df = pd.DataFrame({
    'predictions': y_pred,
    'actual': y_train,
    'age': X_train['age'],
    'bmi': X_train['bmi'],
    'residuals': y_train - y_pred,
})

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='predictions', y='actual',
                data=plot_df, alpha=0.7)

plt.xlabel('Predicted log_charges')
plt.ylabel('Actual log_charges')

plt.show()

sns.scatterplot(x='predictions', y='residuals',
                data=plot_df, alpha=0.7)
plt.show()

test_pred = smoker_model.predict(X_test)
print(mean_squared_error(y_test, test_pred))   # 0.09416078156173806

# Linear regression equation: log_charges = 10.200 + 0.051×age + 0.016×bmi + 2.232×is_smoker