
import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()  # carreglo numpy
print(digits.keys())
print(digits["target"][0])
plt.matshow(digits["images"][0])
plt.show()
# for llave in diabetes.keys():  (diabetes[llave], "/n")
print(digits["target"][108])
plt.matshow(digits["images"][108])
plt.show()