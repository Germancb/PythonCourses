from numpy import random
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(random.logistic(size=1000))
plt.show()