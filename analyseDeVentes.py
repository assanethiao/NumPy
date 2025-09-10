"""
Projet : Analyse de ventes d’un magasin

Objectif :
--Simuler les ventes quotidiennes d’un magasin sur 1 mois (30 jours).
--Calculer les totaux, les moyennes et identifier les meilleurs jours.
--Déterminer quels produits se vendent le mieux.

Tâches à réaliser :
--Crée un tableau NumPy de dimension (30, 5) représentant les ventes journalières de 5 produits (par exemple des valeurs aléatoires entre 0 et 100).
--Calcule :
----le total des ventes par jour (somme sur les colonnes)
----le total des ventes par produit (somme sur les lignes)
--Trouve :
----le jour avec le plus gros chiffre d’affaires
----le produit le plus vendu sur le mois
--Calcule la moyenne de ventes par produit sur le mois.
--Affiche un résumé clair avec ces informations.
"""
import numpy as np
import matplotlib.pyplot as plt

# Liste des produits
mesProduits = np.array(["iphone14", "iphone15", "iphone16", "samsungS28", "samsungA08" ])

# Jours du mois (1 à 30)
jours =  np.arange(1,31)

# Génération aléatoire des ventes journalières (30 jours x 5 produits)
ventesJournalieres = np.random.randint(0, 100, size=150).reshape(30,5)

# Total des ventes par produit sur le mois (somme par colonne)
venteTotalProduitMensuelle = np.sum(ventesJournalieres, 0)

# Total des ventes par jour (somme par ligne)
venteTotalParJourMensuelle = np.sum(ventesJournalieres, 1)

# Initialisation des tableaux max/min pour chaque produit
maxVenteProduit = np.zeros(5, int)
minVenteProduit = np.zeros(5, int)

# Calcul du maximum et minimum par produit
for i in range(5):
    maxVenteProduit[i] = np.max(ventesJournalieres[:,i])
    minVenteProduit[i] = np.min(ventesJournalieres[:,i])

# Initialisation des tableaux max/min pour chaque jour
maxVenteJour = np.zeros(30, int)
minVenteJour = np.zeros(30, int)

# Calcul du maximum et minimum par jour
for i in range(30):
    maxVenteJour[i] = np.max(ventesJournalieres[i,: ])
    minVenteJour[i] = np.min(ventesJournalieres[i,:])

# Création de la figure globale avec taille personnalisée
plt.figure(figsize=(15, 25))


# Graphique 1 : vente totale par jour

plt.subplot(5,2,1)
plt.plot(jours, venteTotalParJourMensuelle, marker="+", color="green", label="Max")
plt.xticks(np.arange(2, 31, 2))            
plt.yticks(np.arange(100, 400, 25))        
plt.xlabel("Jour")
plt.ylabel("Vente par total jour")
plt.title("Évolution de la vente totale par jour")
plt.legend()


# Graphique 2 : minimum et maximum par jour

plt.subplot(5,2,2)
plt.plot(jours, maxVenteJour, marker="o", color="blue", label="Max")  # maximum journalier
plt.plot(jours, minVenteJour, marker="o", color="red", label="Min")   # minimum journalier
plt.xticks(np.arange(2, 31, 2))            
plt.xlabel("Jour")
plt.ylabel("Nombre de vente")
plt.title("Évolution min/max par jour")
plt.legend()


# Graphique 3 : bar chart des ventes totales par produit

plt.subplot(5,2,3)
plt.bar(mesProduits, venteTotalProduitMensuelle, color="purple", edgecolor="orange")
plt.xlabel("Produits")
plt.ylabel("Vente total")
plt.title("Vente total mensuelle")


# Graphique 4 : histogramme des ventes

plt.subplot(5, 2, 4)
plt.hist(ventesJournalieres.flatten(), bins=20, color="orange", edgecolor="blue")  # flatten pour tableau 1D
plt.xticks(np.arange(0, 106, 5))          
plt.xlabel("Ventes")
plt.ylabel("Nombre d'occurrences")
plt.title("Histogramme des ventes par produit")

# Graphique 5,6,7,8,9 : Ventes journalières par produit (graphique séparé pour chaque produit)
colors = ["red", "green", "blue", "purple", "orange"]
for i in range(5):
    plt.subplot(5,2,5+i)
    plt.plot(jours, ventesJournalieres[:,i], marker="o", color=colors[i])
    plt.xticks(np.arange(2, 31, 2))
    plt.xlabel("Jour")
    plt.ylabel("Ventes")
    plt.title(f"Évolution des ventes : {mesProduits[i]}")
    
# Ajustement automatique des espaces entre les subplots
plt.tight_layout()  
plt.show()
