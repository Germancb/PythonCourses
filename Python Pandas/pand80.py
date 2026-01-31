# CORRELACION
import matplotlib.pyplot as plt
import pandas as pd

personas = pd.read_csv("datos/personas.csv")
print(personas)

# Relacion altura peso
plt.scatter(personas["altura"], personas["peso"])
plt.xlabel("Altura (cms)")
plt.ylabel("Peso (kgs)")
plt.show()

# Relacion ingreso y horas trabajadas
plt.scatter(personas["ingreso"], personas["horas_trabajadas"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Horas Trabajadas")
plt.show()

# Relacion Ingreso ausencias
plt.scatter(personas["ingreso"], personas["ausencias"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Ausencias")
plt.show()

#Relacion ingreso peso una ersona
plt.scatter(personas["ingreso"], personas["peso"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Peso (kg)")
plt.show()
 # Matriz de correlacion
matriz = personas.corr() # -1 (existe una relación fuerte)  0   1 (existe relación fuerte)
plt.matshow(matriz, cmap="bwr", vmin=-1, vmax=1)
plt.xticks(range(5), personas.columns, rotation=90)
plt.yticks(range(5), personas.columns)

for i in range(len(matriz.columns)):
    for j in range(len(matriz.columns)):
        plt.text(i, j, round(matriz.iloc[i, j], 2),
                 ha="center", va="center")


plt.colorbar()
plt.show()