from statistics import mode
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

x = numpy.median(speed)
print(x)
x = mode(speed)
print(x)

from scipy import stats
x = stats.mode(speed)
print(x)