import matplotlib.pyplot as plt
import pandas as pd

personas = pd.read_csv("datos/personas.csv")
print(personas)

plt.scatter(personas["altura"], personas["peso"])
plt.xlabel("Altura (cms)")
plt.ylabel("Peso (kgs)")
plt.show()

plt.scatter(personas["ingreso"], personas["horas_trabajadas"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Horas Trabajadas")
plt.show()

plt.scatter(personas["ingreso"], personas["ausencias"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Ausencias")
plt.show()

plt.scatter(personas["ingreso"], personas["peso"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Peso (kg)")
plt.show()

# matriz de correlacion
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
