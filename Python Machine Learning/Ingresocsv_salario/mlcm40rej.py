# Ajustar hiperparametros REJILLA
import pandas as pd 

personas = pd.read_csv("ingresos.csv")
personas

from sklearn.ensemble import RandomForestClassifier

bosque = RandomForestClassifier()
print(bosque.get_params())

# Busqueda cuadrilla o rejilla
from sklearn.model_selection import GridSearchCV

parametros = {"criterion": ("gini", "entropy"),
              "n_estimators" : (10, 20, 30), 
              "max_samples" : (1/3, 2/3)}

#Ejemplos de scoring = "accuracy", "recall", "roc_auc", etc.

rejilla = GridSearchCV(bosque, 
                       parametros, 
                       scoring="accuracy")

rejilla.fit(personas[personas.columns[:-1]].values, 
            personas["ingreso"].values)
print("Rejilla")
print(rejilla)
# Inf busqueda en rejilla
print(sorted(rejilla.cv_results_.keys()))
# rejilla de parametros explorados
sorted(rejilla.cv_results_.keys())
print("scores 4)")
print(rejilla.cv_results_["rank_test_score"])
print(rejilla.cv_results_["mean_test_score"])
print(rejilla.best_score_)
print(rejilla.best_params_)
print("rejilla.predict")
print(rejilla.predict([[50, 16, 1, 1, 40]]))
mejor_bosque = rejilla.best_estimator_
print("Mejor bosque")
print(mejor_bosque.predict([[50, 16, 1, 1, 40]]))   # Llama al mejor modelo
# mejor_bosque = rejilla.best_model_
# print(mejor_bosque.predict([[50, 16, 1, 1, 40]])) 
# Busqueda aleatoria
from sklearn.model_selection import RandomizedSearchCV

parametros = {"criterion": ("gini", "entropy"),
              "n_estimators" : (10, 20, 30), 
              "max_samples" : (1/3, 2/3)}

rejilla_aleatoria = RandomizedSearchCV(bosque, 
                                       parametros,
                                       scoring = "accuracy", 
                                       cv=5, 
                                       n_iter=3)

rejilla_aleatoria.fit(personas[personas.columns[:-1]].values,
                      personas["ingreso"].values)
print("Rejilla aleatoria")
print(rejilla_aleatoria)

# parametros explorados aleatoriamente
rejilla_aleatoria.cv_results_["params"]
print(rejilla_aleatoria.cv_results_["params"])
print("Rejilla aleatoria best score best param)")
print(rejilla_aleatoria.best_score_)
print(rejilla_aleatoria.best_params_)