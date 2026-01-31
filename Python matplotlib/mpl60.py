# GRAFICAS CATEGORICAS

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", context="talk", palette="tab10")
# Datos Categóricos a Visualizar
consumos = sns.load_dataset("tips")

consumos.columns = ["total", "propina", "genero", "fumador",
                    "dia", "tipo", "comensales"]

print(consumos)
# plt.colorbar()
plt.show()
# Gráfica stripplot
sns.catplot(x="dia", y="total", data=consumos,
            kind="strip", hue="comensales", s=7, col="fumador")

sns.catplot(x="dia", y="total", data=consumos,
            kind="strip", jitter=False, hue="comensales", s=7, col="fumador")

plt.show()
# Gráfica swarmplot
sns.catplot(x="dia", y="total", data=consumos,
            kind="swarm", hue="comensales", s=7, col="fumador")
plt.show()
#Boxplot
sns.catplot(x="dia", y="total", data=consumos,
            kind="box", col="fumador")
plt.show()
# Boxenplot
sns.catplot(x="dia", y="total", data=consumos, 
            kind="boxen", col="fumador")
plt.show()
#violinplt
sns.catplot(x="dia", y="total", data=consumos,
            kind="violin")

sns.catplot(x="dia", y="total", data=consumos,
            kind="violin", hue="fumador")
plt.show()

sns.catplot(x="dia", y="total", data=consumos,
            kind="violin", hue="fumador", split=True)

plt.show()
# Pointplot
sns.catplot(x="dia", y="total", data=consumos, 
            kind="point", col="fumador")
plt.show()


# barplot
sns.catplot(x="dia", y="total", data=consumos,
            kind="bar", hue="comensales")
plt.show()

# Countplot
sns.catplot(x="dia", data=consumos,
            kind="count", hue="comensales")
plt.show()

