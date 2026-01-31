# ["especie", "isla", "longitud_pico", "profundidad_pico", "longitud_aleta", "masa", "sexo"]
import matplotlib.pyplot as plt
import seaborn as sns
print(sns.get_dataset_names())   # precargadas en seaborn
pinguinos = sns.load_dataset("penguins")
pinguinos.columns = ["especie", "isla", "longitud_pico", "profundidad_pico",
                     "longitud_aleta", "masa", "sexo"]
print(pinguinos)

sns.set_theme(style="ticks", context="talk")
# sns.set_theme(styles="darkgrid", contet="talk")
relacional = sns.relplot(data=pinguinos,
                        height=7,
                        aspect=1.2,
                        markers=["s", ".", "P", "d"])   # relplot relaciones solo datso numericos
relacional.set(title="Análisis de Pingüinos")
relacional.set_ylabels("Variables")
relacional.set_xlabels("Número de Pingüino")
plt.show()

print(">>>>>>>>>>>>>>>>>>>> SIMPLE")

sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta")
plt.show()

print(">>>>>>>>>>>>>>>>>>>> MATIZ Y TAMAÑO FIJO")

fig = sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="masa",
           size="masa",
           sizes=(100, 500))   #hue/size matiz/tamaño asiciadad a la masa de los p

fig.savefig("out.png", transparent=True) 
plt.show()

sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="especie",
           s=300)
plt.show()
print(">>>>>>>>>>>>>>>>>>>> REJILLA, TAMAÑO PERSONALIZADO Y ESTILO")

sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="especie",
           row="sexo",
           size="masa",
           sizes=(100, 500),
           style="sexo")
plt.show()
print(">>>>>>>>>>>>>>>>>>>> SIMPLE")

sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta")
plt.show()
print(">>>>>>>>>>>>>>>>>>>> MATIZ Y TAMAÑO FIJO")

fig = sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="masa",
           size="masa",
           sizes=(100, 500))
plt.show()
fig.savefig("out.png", transparent=True) 


sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="especie",
           s=300)
plt.show()
print(">>>>>>>>>>>>>>>>>>>> REJILLA, TAMAÑO PERSONALIZADO Y ESTILO")

sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="especie",
           row="sexo",
           size="masa",
           sizes=(100, 500),
           style="sexo")

plt.show()

sns.relplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="especie",
           col="isla",
           row="sexo",
           size="masa",
           sizes=(100, 500),
           style="sexo")

plt.show()