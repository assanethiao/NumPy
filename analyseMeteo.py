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

joursParMois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mois = np.array([
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin","Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
])
tempMins = [2, 3, 5, 8, 12, 15, 18, 18, 15, 10, 6, 3]
tempMaxs = [7, 9, 13, 16, 20, 29, 35, 32, 24, 18, 12, 8]

nombreJoursTotal=365
temperatures = []

for i in range(12):
    nbJours = joursParMois[i]
    tMin = tempMins[i]
    tMax = tempMaxs[i]
    tempMois = np.random.randint(tMin, tMax + 1, size=nbJours)
    temperatures.extend(tempMois)

tabTemp = np.array(temperatures)

tempMax = np.max(tabTemp)
jourTempMax = np.argmax(tabTemp)

jourCumul = 0
moisTempMax = 0
jourDansMoisMax = 0

for i, nbJours in enumerate(joursParMois):
    if jourTempMax < jourCumul + nbJours:
        moisTempMax = i + 1
        jourDansMoisMax = jourTempMax - jourCumul + 1
        break
    jourCumul += nbJours

tempMin = np.min(tabTemp)
jourTempMin = np.argmin(tabTemp)

jourCumul = 0
moisTempMin = 0
jourDansMoisMin = 0

for i, nbJours in enumerate(joursParMois):
    if jourTempMin < jourCumul + nbJours:
        moisTempMin = i + 1
        jourDansMoisMin = jourTempMin - jourCumul + 1
        break
    jourCumul += nbJours

tabtempMoyenne = np.zeros(12).reshape(1, 12)
compteurJour = 0
for i in range(12):
    tempDuMoisCourant = 0
    moyenneDuMois = 0
    for j in range(joursParMois[i]):
        tempDuMoisCourant = tempDuMoisCourant + tabTemp[compteurJour + j]

    compteurJour = compteurJour + j
    moyenneDuMois = tempDuMoisCourant /(j+1)
    # a revoir
    tabtempMoyenne[0, i] = moyenneDuMois
    print(moyenneDuMois)
    print(tabtempMoyenne[0,1])

        
print(tabTemp)


print("Température max :", tempMax)
print("Jour de l'année :", jourTempMax + 1)
print(f"Date du jour le plus chaud : {jourDansMoisMax} {mois[moisTempMax -1]} (mois {moisTempMax})")

print("Température min :", tempMin)
print("Jour de l'année :", jourTempMin + 1)
print(f"Date du jour le plus froid : {jourDansMoisMin} {mois[moisTempMin -1]} (mois {moisTempMin})")
