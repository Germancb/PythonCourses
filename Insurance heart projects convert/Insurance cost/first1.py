import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the insurance dataset
insurance = pd.read_csv('insurance.csv')

num_insurance = insurance.select_dtypes(include='number')  # No esta en las instrucciones

# Now compute correlation a los valores numéricos
correlations = num_insurance.corr()
print(correlations)
sns.heatmap(correlations, cmap='Blues', annot=True)
plt.show()

insurance["is_smoker"] = (insurance["smoker"] == "yes")
print(insurance["is_smoker"])

