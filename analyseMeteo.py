"""
Projet : Analyse météo avec NumPy

Objectif :
--Générer des données de température pour une ville pendant 1 an (365 jours).
--Extraire les jours les plus chauds, les plus froids, et la température moyenne par mois.
--Identifier les vagues de chaleur (plus de 30°C trois jours d’affilée).

Tâches à réaliser :
--Crée un tableau NumPy de 365 valeurs représentant les températures journalières (par exemple aléatoires entre -5°C et 40°C).
--Trouve :
----la température maximale et son jour
----la température minimale et son jour
--Découpe les données en 12 mois (attention : tous les mois n’ont pas le même nombre de jours !).
--Calcule la moyenne de température pour chaque mois.
--Détecte s’il existe une vague de chaleur (au moins 3 jours > 30°C consécutifs).
--Affiche un résumé des résultats.
"""

import numpy as np
import matplotlib.pyplot as plt

joursParMois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mois = np.array([
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin","Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
])

# les temperatures mins et max pour chaque mois
tempMins = [2, 3, 5, 8, 12, 15, 18, 18, 15, 10, 6, 3]
tempMaxs = [7, 9, 13, 16, 20, 29, 35, 32, 24, 18, 12, 8]

nombreJoursTotal=365
temperatures = []

# attribuer aleatoirement chaque jour (les 365 ) a une temperature
for i in range(12):
    nbJours = joursParMois[i]
    tMin = tempMins[i]
    tMax = tempMaxs[i]
    tempMois = np.random.randint(tMin, tMax + 1, size=nbJours)
    temperatures.extend(tempMois)
    
# transformer notre liste 'temperatures' en tableau NumPy
tabTemp = np.array(temperatures)

# chercher la temperature max et son jour dans l'annee
tempMax = np.max(tabTemp)
jourTempMax = np.argmax(tabTemp)

jourCumul = 0
moisTempMax = 0
jourDansMoisMax = 0
# chercher le ieme jour dans l'annee ou la temperature est max
for i, nbJours in enumerate(joursParMois):
    if jourTempMax < jourCumul + nbJours:
        moisTempMax = i + 1
        jourDansMoisMax = jourTempMax - jourCumul + 1
        break
    jourCumul += nbJours

# chercher la temperature min et son jour dans l'annee
tempMin = np.min(tabTemp)
jourTempMin = np.argmin(tabTemp)

jourCumul = 0
moisTempMin = 0
jourDansMoisMin = 0
# chercher le ieme jour dans l'annee ou la temperature est min
for i, nbJours in enumerate(joursParMois):
    if jourTempMin < jourCumul + nbJours:
        moisTempMin = i + 1
        jourDansMoisMin = jourTempMin - jourCumul + 1
        break
    jourCumul += nbJours

# faire la moyenne mensuelle des temperatures
tabtempMoyenne = np.zeros(12).reshape(1, 12)
compteurJour = 0
for i in range(12):
    tempDuMoisCourant = 0
    moyenneDuMois = 0
    for j in range(joursParMois[i]):
        tempDuMoisCourant = tempDuMoisCourant + tabTemp[compteurJour + j]

    compteurJour += joursParMois[i]
    moyenneDuMois = tempDuMoisCourant / joursParMois[i]
    tabtempMoyenne[0, i] = moyenneDuMois

# la figure principal
plt.figure(figsize=(14,10))  # taille de la figure globale

# visuel des températures journalières (courbe)
plt.subplot(2, 2, 1)  # (nblignes, nbcolonnes, position)
plt.plot(tabTemp, label="Température journalière")
plt.axhline(tempMax, color="red", linestyle="--", label="Max annuel")
plt.axhline(tempMin, color="blue", linestyle="--", label="Min annuel")
plt.xlabel("Jour de l'année")
plt.ylabel("Température (°C)")
plt.title("Variation journalière")
plt.legend()

# Moyenne mensuelle (bar chart)
plt.subplot(2, 2, 2)
plt.bar(mois, tabtempMoyenne.flatten(), color="orange")
plt.xlabel("Mois")
plt.ylabel("Température moyenne (°C)")
plt.title("Température moyenne par mois")
plt.xticks(rotation=45)

# Histogramme des températures
plt.subplot(2, 2, 3)
plt.hist(tabTemp, bins=20, color="green", edgecolor="black")
plt.xlabel("Températures (°C)")
plt.ylabel("Nombre de jours")
plt.title("Distribution des températures annuelles")

# Min/Max par mois
plt.subplot(2, 2, 4)
plt.plot(mois, tempMins, marker="o", color="blue", label="Min")
plt.plot(mois, tempMaxs, marker="o", color="red", label="Max")
plt.xlabel("Mois")
plt.ylabel("Température (°C)")
plt.title("Évolution min/max par mois")
plt.xticks(rotation=45)
plt.legend()

#on ajuste l'emplacement des 4 figures
plt.tight_layout() 
plt.show()
