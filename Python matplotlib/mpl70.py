# Graficos relacionales lineas y combinadas line y scatter
# ["especie", "isla", "longitud_pico", "profundidad_pico", "longitud_aleta", "masa", "sexo"]
import matplotlib.pyplot as plt
import seaborn as sns
pinguinos = sns.load_dataset("penguins")
pinguinos.columns = ["especie", "isla", "longitud_pico", "profundidad_pico",
                     "longitud_aleta", "masa", "sexo"]
print(pinguinos)

sns.relplot(data=pinguinos,
           x="especie",
           y="masa",
           kind="line",
           hue="sexo",
           style="sexo",
           ci="sd")
plt.show()

fig = sns.relplot(data=pinguinos,
           x="profundidad_pico",
           y="longitud_pico",
           kind="line",
           hue="especie",
           style="especie",
           row="especie",
           color="cyan",
           ci="sd")

fig.savefig("out3.png", transparent=True) 

plt.show()

figura, ejes = plt.subplots(1, 2, figsize=(15, 5))

sns.lineplot(data=pinguinos,
           x="especie",
           y="masa",
           hue="sexo",
           style="sexo",
           ax=ejes[0])

    
sns.scatterplot(data=pinguinos,
           x="longitud_pico",
           y="longitud_aleta",
           hue="especie",
           s=300,
           ax=ejes[1])

figura.savefig("out2.png", transparent=True) 

plt.show()
