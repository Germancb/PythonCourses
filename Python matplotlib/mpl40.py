import numpy as np
import matplotlib.pyplot as plt
# Diagrma de ajas Box plot
edades = np.array([4, 17, 29, 33, 50, 51, 61, 71, 85, 92, 99])
print(np.min(edades), " ", np.quantile(edades, 0.25), " ", np.median(edades), " ", np.quantile(edades, 0.75), " ", np.max(edades))

plt.yticks(np.arange(0, 110, 5))
plt.grid(True)
plt.boxplot(edades)
plt.show()

print((np.min(edades), np.quantile(edades, 0.25), np.median(edades),
np.quantile(edades, 0.75), np.max(edades)))

# datos anormales o atipicos  prueba de Tukey
edades = np.array([6, 
                   41, 51, 51, 52, 54, 57, 60, 61, 65, 
                   95, 100])

plt.grid(True)
plt.yticks(np.arange(0, 110, 5))
plt.boxplot(edades)
plt.show()