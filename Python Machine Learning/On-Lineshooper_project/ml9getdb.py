import pandas as pd

# URL del dataset en el repositorio de UCI Machine Learning
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00483/online_shoppers_intention.csv"

df_ecommerce = pd.read_csv(url)

print("--- Dataset de Intención de Compra ---")
print(df_ecommerce.head())
print(f"\nDimensiones: {df_ecommerce.shape}")
