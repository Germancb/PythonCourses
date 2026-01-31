# Distribucion Normal
import numpy as np 
import matplotlib.pyplot as plt

# altura promedio
mu = 170 

# desviación estándar
sigma = 8 

# generación de 100 mil alturas aleatorias
n = 100000
alturas = np.random.normal(mu, sigma, n)

# Creación de histograma
plt.figure(figsize=(9,3.5))
conteo, x, barras = plt.hist(alturas, 100, density=True, 
                             color="pink", alpha=0.7)

# Campana utilizando la función de densidad de probabilidad
plt.plot(x,
         1 / (sigma*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mu)/sigma)**2),
         linewidth=1, color="purple")

# Dibujando las desviaciones estándar y la media
sigmas = [mu - 3*sigma, mu - 2*sigma, mu - sigma, mu,
          mu + sigma, mu + 2*sigma, mu + 3*sigma]
for s in sigmas:
    plt.axvline(s, color = "teal", linewidth=1.5, linestyle="dashed")

plt.yticks([]) 
plt.xticks([]) 
plt.box(False)
plt.show()
print("\n*** Regla Empírica 68-95-99.7 de la Distribución Normal ***\n")
print(mu - sigma, "-", mu + sigma, "cm\t", 
      mu - 2*sigma, "-", mu + 2*sigma, "cm\t",
      mu - 3*sigma, "-", mu + 3*sigma, "cm")
print((np.where(((mu - sigma) < alturas) & 
                (alturas < (mu + sigma)), 1, 0).sum()*100)/n, "%\t",  
      (np.where(((mu - 2*sigma) < alturas) & 
                (alturas < (mu + 2*sigma)), 1, 0).sum()*100)/n, "%\t",  
      (np.where(((mu - 3*sigma) < alturas) & 
                (alturas < (mu + 3*sigma)), 1, 0).sum()*100)/n, "%\t")