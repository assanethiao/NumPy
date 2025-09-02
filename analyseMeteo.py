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
