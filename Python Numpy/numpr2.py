from numpy import random  #visualitation
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.logistic(size=1000))   ## , hist=False)
plt.show()
