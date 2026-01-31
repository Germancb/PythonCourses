import numpy as np
#arr=np.array([[1,2,3,4],[5,6,7,8]])
pesos = [5,15,25,30,40, 55, 80, 90, 170]
print("Rango :", np.max(pesos) - np.min(pesos))

print("Varianza poblacional :", np.var(pesos))
print("Varianza muestral :", np.var(pesos, ddof = 1))

print("Desv Standard poblacional :", np.std(pesos))
print("Desv Stand muestral :", np.std(pesos, ddof = 1))
Q1=np.percentile(pesos, 25)
Q3= np.percentile(pesos, 75) 
print("Rango intercuantilico: ", Q3-Q1)