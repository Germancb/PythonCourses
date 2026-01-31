from numpy import random
x = random.uniform(size=(2, 3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(random.uniform(size=1000))
plt.show()