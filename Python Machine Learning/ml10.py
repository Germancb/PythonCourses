from scipy import stats
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept
speed = myfunc(10)
#mymodel1 = map(myfunc, x)   # functionto apply a specified function to each item in an iterable (like list). Return an iterator
#mymodel = list(mymodel1)
plt.scatter(x, y)
# plt.plot(x, mymodel)
plt.show()

print(speed)
print(slope)
print(intercept)
print(r) 
print(std_err)