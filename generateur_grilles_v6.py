
import pandas as pd
import random
from collections import Counter

def charger_donnees(fichier="data/euromillions.csv"):
    df = pd.read_csv(fichier, sep=';')
    return df

def calculer_frequences(df):
    nums = df[['N1', 'N2', 'N3', 'N4', 'N5']].values.flatten()
    etoiles = df[['E1', 'E2']].values.flatten()
    freq_nums = Counter(nums)
    freq_etoiles = Counter(etoiles)
    return freq_nums, freq_etoiles

def ponderer_numeros(freq, total_tirages):
    pond = {}
    for num in range(1, 51):
        pond[num] = freq.get(num, 0) / total_tirages
    return pond

def ponderer_etoiles(freq, total_tirages):
    pond = {}
    for e in range(1, 13):
        pond[e] = freq.get(e, 0) / total_tirages
    return pond

def generer_une_grille(pond_nums, pond_etoiles):
    nums_pool = sorted(pond_nums.items(), key=lambda x: x[1], reverse=True)
    etoiles_pool = sorted(pond_etoiles.items(), key=lambda x: x[1], reverse=True)

    # Choisir 20 numéros pondérés et tirer 5 de manière équilibrée
    candidats = [num for num, _ in nums_pool[:25]]
    grille_numeros = sorted(random.sample(candidats, 5))

    # Pareil pour les étoiles
    candidats_etoiles = [e for e, _ in etoiles_pool[:6]]
    grille_etoiles = sorted(random.sample(candidats_etoiles, 2))

    return grille_numeros, grille_etoiles

def generer_grilles(nb=5):
    df = charger_donnees()
    total = len(df)
    freq_nums, freq_etoiles = calculer_frequences(df)
    pond_nums = ponderer_numeros(freq_nums, total)
    pond_etoiles = ponderer_etoiles(freq_etoiles, total)

    grilles = []
    for _ in range(nb):
        nums, etoiles = generer_une_grille(pond_nums, pond_etoiles)
        grilles.append((nums, etoiles))
    return grilles

if __name__ == "__main__":
    grilles = generer_grilles(5)
    for i, (nums, etoiles) in enumerate(grilles, 1):
        print(f"{i}. {nums} | Étoiles : {etoiles}")
