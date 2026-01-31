import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(slope)
print(intercept)
print(r)   # coeficiente de correlacion
print(p)    # valor de p se puede usar en pruebas de hipotesis (Signficancia estadistica de la pendiente)
print(std_err)

def myfunc(x):
  return slope * x + intercept

# mymodel = list(map(myfunc, x))    # crea lista con valores de y calculados y con map retorna una lista
mymodel1 = map(myfunc, x)   # functionto apply a specified function to each item in an iterable (like list). Return an iterator
mymodel = list(mymodel1)  # crea lista con los valores de y calculados
# print(mymodel)   Valores de y calculados con slope e interce


