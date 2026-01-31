from numpy import random
x = random.binomial(n=10, p=0.5, size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(random.binomial(n=10, p=0.5, size=1000), kde=False)
plt.show()
