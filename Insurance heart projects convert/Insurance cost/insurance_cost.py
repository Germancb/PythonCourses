c
# %%Load the insurance dataset
insurance = pd.read_csv('insurance.csv')
# %% exploratory data analysis
print(insurance.head())
insurance.info()
insurance.describe()
insurance.hist('charges')
plt.show()  # histogram of charges

# %% Logarttm histogram
insurance["log_charges"] = np.log2(insurance["charges"])
insurance.hist("log_charges")
plt.show()  # Histograma logarítmico
# %% include only numeric columns para calcular e imprimir correlaciones y su diagrama matriz
print(insurance.dtypes)
ins2=insurance.select_dtypes(include=np.number)
correlations = ins2.corr()
print(correlations)
sns.heatmap(correlations, cmap='Blues', annot=True)
plt.show()
# %% Let's visualize relationships using a pair plot:
insurance_numeric = ins2[['age', 'bmi', 'children', 'charges', 'log_charges']]
sns.pairplot(insurance_numeric, kind='scatter', plot_kws={'alpha': 0.4})
plt.show()   # corre todo
# %% Now let's examine our categorical variables using box plots:
insurance.boxplot(column=["log_charges"], by="sex")
plt.show()
insurance.boxplot(column=["log_charges"], by="smoker")
plt.show()
insurance.boxplot(column=["log_charges"], by="region")
plt.show()
# %% Splitting the data up into a training and test set
insurance["is_smoker"] = (insurance["smoker"] == "yes")
# %% insurance["is_male"] = (insurance['sex'] == 'male')
# %%  insurance['is_west'] = ((insurance['region'] == 'northwest') | (insurance['region'] == 'southwest'))
X = insurance[["age", "bmi", "is_smoker"]]
y = insurance["log_charges"]
# 75% for training set, 25% for test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=42)
# %% Building the Model   # Now we'ii create and train our linear model
insurance_model = LinearRegression()
insurance_model.fit(X_train, y_train)
print(insurance_model.coef_)   #  [0.0508618  0.01563733 2.23214787]
# %% Let's evaluate our model's performance:
y_pred = insurance_model.predict(X_train)
train_mse = mean_squared_error(y_train, y_pred)
print("train_mse ", train_mse)   #0.447919196329921
# %% MSE on the original scale for the insurance charges
train_mse_orig_scale = np.exp(mean_squared_error(y_train, y_pred))
print("train_mse_orig_scale ", train_mse_orig_scale)   #1.565052228580154
train_r2 = r2_score(y_train, y_pred)
print("Train_R2 ", train_r2) #  0.743333600772825
# %% Residual DIiagnostic. # Create a DataFrame with predictions and actual values for easier plotting
plot_df = pd.DataFrame({
    'predictions': y_pred,
    'actual': y_train,
    'is_smoker': X_train['is_smoker'],
    'age': X_train['age'],
    'bmi': X_train['bmi'],
    'residuals': y_train - y_pred,
})
# %% Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='predictions', y='actual',
                data=plot_df, alpha=0.7)
plt.xlabel('Predicted log_charges')
plt.ylabel('Actual log_charges')
plt.show()
# %% Let's examine the residuals more closely:
sns.scatterplot(x='predictions', y='residuals',data=plot_df, alpha=0.7)
plt.show()
# %% Interpreting the Model  Let's interpret our model coefficients
cdf = pd.DataFrame(insurance_model.coef_, X.columns, columns=['Coef'])
print(cdf)
#               Coef
# age        0.050862
# bmi        0.015637
# is_smoker  2.232148
print("Intercept ",insurance_model.intercept_)
# log_charges = 10.200 + 0.051×age + 0.016×bmi + 2.232×is_smoker
# %% Final model evaluation
test_pred = insurance_model.predict(X_test)
print(mean_squared_error(y_test, test_pred))  #  0.4529281560931769
# %% Putting the outcome (in log-terms) back into the original scale
print(np.exp2(mean_squared_error(y_test, test_pred)))  # 1.368815646563475
# %% Segmentation by smoker status
smokers_df = insurance[insurance["is_smoker"] == True]
X = smokers_df[["age", "bmi"]]
y = smokers_df["log_charges"]
# 75% for training set, 25% for test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=42)
smoker_model = LinearRegression()
smoker_model.fit(X_train, y_train)
print(smoker_model.coef_)    # ([0.01282851, 0.07098738])
y_pred = smoker_model.predict(X_train)
train_mse = mean_squared_error(y_train, y_pred)
print("train_mse", train_mse)   # 0.07046354357369701
train_r2 = r2_score(y_train, y_pred)
print("train_r2", train_r2)    #0.7661650418251629
# %% Create a DataFrame with predictions and actual values for easier plotting
plot_df = pd.DataFrame({
    'predictions': y_pred,
    'actual': y_train,
    'age': X_train['age'],
    'bmi': X_train['bmi'],
    'residuals': y_train - y_pred,
})
# %% Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='predictions', y='actual', data=plot_df, alpha=0.7)
plt.xlabel('Predicted log_charges')
plt.ylabel('Actual log_charges')
plt.show()

sns.scatterplot(x='predictions', y='residuals', data=plot_df, alpha=0.7)
plt.show()
test_pred = smoker_model.predict(X_test)
print(mean_squared_error(y_test, test_pred))  # 0.09416078156173806