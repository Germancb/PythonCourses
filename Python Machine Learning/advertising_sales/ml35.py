import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('advertising_sales.csv')
X = dataset.iloc[:,1:4]
y= dataset['Sales']

X_train, X_test, y_train, y_test =train_test_split(X,y)

lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred = lin.predict(X_test)

coef = lin.coef_
components = pd.DataFrame(zip(X.columns,coef),columns=['component','value'])
components = components._append({'component':'intercept','value':lin.intercept_}, ignore_index=True)
print(components)