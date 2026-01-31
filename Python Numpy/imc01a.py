
import numpy as np

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78] )

peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])   

print(np.stack((altura,peso), axis=0))
print(np.concatenate((altura,peso)))

union = np.stack((altura,peso), axis=0)
print(union)

separados = np.split(union, 2)
print(separados)

