import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

from scipy import stats
# stats.describe(speed, ddof=0).variance
print(stats.describe(speed, ddof=0).variance)  # ddof=0 Varianza poblacional ddof=1 Muestral por defecto en scipy
# y = stats.describe(speed)   

x = stats.tvar(speed)   # Varianza muestral
print('Varianza Muestral',x)
print(stats.describe(speed, ddof=1).variance)

