# CROSS VALIDATION
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

personas = pd.read_csv("salario.csv")

bosque = RandomForestClassifier()

bosque.fit(personas[["edad", "estudio"]].values,
          personas["ingreso"].values)

print(bosque.score(personas[["edad", "estudio"]].values,
                  personas["ingreso"].values))  #0.97

print(cross_val_score(bosque,
                     personas[["edad", "estudio"]].values,
                     personas["ingreso"].values,
                     cv=5))

print(cross_val_score(bosque,
                     personas[["edad", "estudio"]].values,
                     personas["ingreso"].values,
                     cv=5).mean())   # 0.76