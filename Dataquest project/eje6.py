#%% Cargar datos
import pandas as pd
import matplotlib.pyplot as plt

star_wars = pd.read_csv("StarWars.csv", encoding="ISO-8859-1")

print(star_wars.head())   # ← línea 1
star_wars["Age"].hist(bins=10)   # ← línea 2
plt.show()   # ← línea 3

# %%
