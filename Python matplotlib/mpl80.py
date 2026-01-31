
import matplotlib.pyplot as plt
from sklearn import datasets

diabetes = datasets.load_diabetes(as_frame=True)  # como DataFrame de pandas
print(diabetes.keys())
for llave in diabetes.keys():
    print(diabetes[llave], "/n")