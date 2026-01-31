# %% Impora librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
star_wars = pd.read_csv("StarWars.csv", encoding="ISO-8859-1")
print(star_wars.head())
print(star_wars.shape)
# %% Histograma
# plthist(star_wars, bins=8, color='skyblue', edgecolor='black')

# Add labels and title
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram Example")

# Show the plot
# plt.show()
star_wars.info()
print(star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].value_counts(dropna=False))
print(star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].value_counts(dropna=False))
yes_no = {"Yes": True, "No": False, True: True, False: False} # True and False keys ensure correct values aren't overwritten if cell is run more than once

yes_no = {"Yes": True, "No": False, True: True, False: False} # True and False keys ensure correct values aren't overwritten if cell is run more than once

for col in [
    "Have you seen any of the 6 films in the Star Wars franchise?",
    "Do you consider yourself to be a fan of the Star Wars film franchise?",
    "Are you familiar with the Expanded Universe?",
    "Do you consider yourself to be a fan of the Star Trek franchise?"
    
    ]:
    star_wars[col] = star_wars[col].map(yes_no, na_action='ignore')

print(star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].value_counts(dropna=False))

movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True,
    True: True,
    False: False
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)
    
print(star_wars.iloc[:,3:9].head())

star_wars = star_wars.rename(columns={
        "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
        "Unnamed: 4": "seen_2",
        "Unnamed: 5": "seen_3",
        "Unnamed: 6": "seen_4",
        "Unnamed: 7": "seen_5",
        "Unnamed: 8": "seen_6"
        })

print(star_wars.iloc[:,3:9].head())
# %%
