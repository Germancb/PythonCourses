import matplotlib
# import matplotlib.plot as plt
import matplotlib.pyplot as plt

import matplotlib.ticker as maticker
import numpy as np 

# Create random variable:
data = np.random.normal(0, 3, 800)

# Create a Figure and multiple subplots containing Axes:
fig, ax = plt.subplots()
weights = np.ones_like(data) / len(data)

# Create Histogram Axe:
ax.hist(data, bins=5, weights=weights)
ax.yaxis.set_major_formatter(maticker.PercentFormatter(xmax=1.0, decimals=1))

plt.title('Histogram Plot')
plt.show()