#!/usr/bin/env python
# coding: utf-8

# # Bonnes pratiques du codage

# ## Lisibilité et mise en page du code
# Voici une liste non-exhaustive de conseils contribuant à améliorer la lisibilité d'un code et, partant, la facilité à y trouver une erreur de syntaxe, un dysfonctionnement, ou encore à l'étendre ou le partager.

# #### En-tête de fichiers
# Pour tout nouveau fichier, ajouter une introduction descriptive en commentaire :
# - nom du programme
# - date de création
# - nom de l'auteur·rice (et adresse mail)
# - établissement ou entreprise où le programme a été développé

# #### Nommage des variables et des fonctions
# Le nom d'une variable ou d'une fonction doit clairement informer sur son rôle dans le programme.
# 
# <span style="color:green">Facile à lire</span>
# ```python
# variable_facile_a_lire = 20/20
# ```
# 
# <span style="color:red">A proscrire</span>
# ```python
# c = 2 # c représente telle grandeur et il faudra revenir à cette ligne pour le savoir
# variableinutilementillisible = 0/20
# 
# ```
# ---
# <span style="color:green">Facile à lire</span>
# ```python
# def estimation_de_telle_grandeur (mesure_truc, parametre_machin) :
#     # cette fonction calcule une estimation de telle grandeur 
#     # en fonction de la mesure truc et du parametre machin
#     ...
#     return estimation
# ```
# <span style="color:red">A proscrire</span>
# ```python
# def fonction1 (arg1, arg2) :
#     # cette fonction calcule une estimation de telle grandeur en fonction de arg1 et arg2
#     # arg1 représente la mesure truc
#     # arg2 représente le paramètre machin
#     ...
#     return output
# ```
# 
# 

# #### Commenter le code
# Un programme convenablement structuré se présente sous la forme d'une __séquence de fonctions__ dont le nom et celui des arguments sont explicites. 
# Il se lit donc comme un __pseudo-code__ qui doit pouvoir se passer de commentaire.
# 
# Les commentaires doivent trouver leur place
# - au début des blocs d'instructions (délimités par des sauts de ligne) 
# - à la tête du corps des fonctions : doivent figurer la description de la fonctionnalité, celles des variables d'entrées et de sortie.

# #### Où mettre les espaces ? 
# 
# 
# Utiliser des espaces pour séparer les variables des opérateurs.
# 
# <span style="color:green">Facile à lire</span>
# ```python
# if (a + 5 < ma_fonction (arg1, arg2.method () + 4))
# ```
# <span style="color:red">Moins lisible</span>
# ```python
# if a+5<ma_fonction(arg1,arg2.method()+ 4)
# ```
# ---
# Utiliser un espace avant une parenthèse d'ouverture lors de l'appel de fonctions ou de l'indexation :
# 
# <span style="color:green">Facile à lire</span>
# ```python
# ma_fonction (arg1, arg2, arg3)
# ma_liste [0]
# mon_tuple [1]
# mon_dictionnaire ['deux']
# ```
# <span style="color:red">Moins lisible</span>
# ```python
# ma_fonction(arg1,arg2,arg3)
# ma_liste[0]
# mon_tuple[1]
# mon_dictionnaire['deux']
# ```
# Consigne non consensuelle. A essayer

# #### Où placer des sauts de lignes ?
# Les sauts de lignes permettent de regrouper les instructions en __blocs cohérents__.
# 
# En revanche, sauter plusieurs lignes risque de morceler le code et nuire à sa lisibilité.
# 
# Il est impératif de sauter une ligne __entre différentes fonctions__.
