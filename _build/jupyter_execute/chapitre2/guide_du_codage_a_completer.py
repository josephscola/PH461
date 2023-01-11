#!/usr/bin/env python
# coding: utf-8

# # Guide pratique du codage

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

# ## Bonnes pratiques de codage
# Ces consignes visent à __se conformer aux principes de modularité__. 
# L'objectif est d'ainsi faciliter le codage, le débuggage, l'extension ou l'intégration du programme dans des projets futurs.

# ### Organiser le dossier de son projet
# Donner au répertoire de travail la structure suivante :
# - __1 répertoire projet__ contenant le _jupyter  notebook_ du projet
#     - __1 sous-répertoire module__ pour les fonctions spécifiques, structuré comme un module après validation dans jupyter-notebook
#     - __1 sous-répertoire data__ pour les données d'entrée
#     - __1 sous-répertoire output__ pour les données de sortie
# - __1 répertoire routines__ dédié aux fonctions appelées par plusieurs projets et localisé au même niveau d'arborescence que les projets.

# ### Ne pas se précipiter sur son clavier
# Même si le codage peut s'avérer être la partie la plus attractive du développement du projet, il convient de __toujours structurer son projet/programme dans son ensemble__ avant de commencer à coder. Cela revient à rédiger un cahier des charges. Il sera peut-être partiellement modifié en cours de développement mais les grandes lignes doivent être connues avant d'écrire la première ligne de code.
# - Identifier les objectifs :
#     - quelles informations __en entrée__ du programme
#     - quelles données __en sortie__ du programme
#     - quels __formats__ des données en entrée et en sortie (vecteurs, matrices, chaînes de caractères, images, ...)
#     - quelles __opérations__ réalisées (lecture/écriture de fichiers, affichage terminal, figures, ...)
#     - identification des __ressources à disposition__ (temps, espace mémoire, capacité processeur, ...)
# - Identifier les fonctionnalités
#     - __Décomposer__ chaque fonctionnalités en fonctions et sous-fonctions (et sous-sous-fonction...)
#     - __Se documenter__ sur les fonctionnalités encore non maîtrisées (et il y en aura toujours)
#     - Certaines fonctionnalités ont-elles déjà été codées ?
# - Pour chaque fonctionnalité, identifier :
#     - les __cas de figure__ pris en charges et les __exceptions__
#     - les __entrées__ et les __sorties__
# - Anticiper des __extensions futures__
# 
# <div class="alert alert-block alert-info">
# <b>ATTENTION :</b> cette étape peut prendre plusieurs heures voire plusieurs jours.
# </div>

# _Exemple_ : __Projet Notation_scientifique__
# > Objectifs :
# - Le programme doit afficher un résultat expérimental dans la notation scientifique. 
# - Un résultat expérimental est constitué de la valeur mesurée et de l'incertitude de mesure.
# - Le nombre de chiffres significatifs doit s'accorder à l'ordre de grandeur de l'incertitude.
# - L'incertitude a été arrondie par l'expérimentateur·rice (1, 2, 3 chiffres significatifs suivant le contexte)
# - L'affichage doit inclure l'unité de la grandeur mesurée.
# 
# > Données en entrées :
# - valeur mesurée (float)
# - incertitude (float)
# - unité (string)
# 
# > Données en sorties :
# - chaîne de caractères formattée (_e.g._ $X = (1.234 \pm 0.056)\cdot 10 ^{-6} \quad \mathrm{m}$)
# 
# > Opérations réalisées :
# - pas d'opérations
# 
# > Ressources à disposition : 
# - projet très léger &rarr; ressources illimitées

# > Fonctionnalités :
# - déterminer l'ordre de grandeur de la valeur mesurée pour le factoriser avec l'incertitude &rarr; A CODER : ordre_de_grandeur
#     - entrée : valeur (float)
#     - sortie : exposant d'une puissance de 10 (int)
# - déterminer l'ordre de grandeur de l'incertitude &rarr; A CODER : ordre_de_l_erreur
#     - entrée : erreur (float)
#     - sortie : exposant d'une puissance de 10 (int)
# - arrondir la valeur mesurée en fonction de l'arrondi  &rarr; fonction numpy.round ()
# - factoriser la puissance de 10 et construire la chaîne de caractère au format notation scientifique &rarr; A CODER : notation_scientifique (fonction principale)
#     - entrée : valeur mesurée, incertitude, unité
#     - sortie : chaîne de caractère au format notation scientifique
#     - pas d'avertissement en cas d'incohérence entre la valeur et l'erreur (val < err)
#    
# > Extensions futures :
# - arrondir automatiquement l'incertitude expérimentale à N chiffres significatifs &rarr; à intégrer à l'intérieur de la fonction ordre_de_l_erreur.

# ### Coder en respectant la structure du programme
# Une fois établie la décomposition du programme en une cascade de sous-fonctions, le codage doit commencer par les fonctions de plus bas niveau :
# - elles sont simples et pourront être testées facilement
# - elles seront réutilitées par les fonctions de niveau supérieur
# 
# Ainsi, la complexité du codage sera maintenu à un niveau faible, ce qui favorise la rapidité et la fiabilité.

# In[1]:


# sous-fonctions
import numpy as np

def ordre_de_grandeur (x):
    
    return res

def ordre_de_l_erreur (err, debug = False):    
    
    return odgerr


# ### Contrôler son programme
# Après avoir contrôlé la sytnaxe et quand le programme ne retourne plus d'erreur, il est indispensable de s'assurer que le résultat est conforme aux objectifs. 
# Pour cela, il convient d'établir un programme de test visant à contrôler l'exactitude de _toutes les fonctionnalités_, _dans un maximum de cas de figure_ envisageable.
# 
# Dans la mesure du possible, le test et la correction d'erreur doit être faite au __fur et à mesure__; les blocs à testers s'en trouvent plus courts.

# _Exemple_ : __Projet Notation_scientifique__
# 
# Test des sous-fonctions
# 

# In[2]:


# test de ordre_de_grandeur


# In[3]:


# test de ordre_de_l_erreur


# _Exemple_ : __Projet Notation_scientifique__
# 
# Fonction principale appelant les sous-fonctions.

# In[4]:


def represente_resultat_mesure_ (val, err, unit, debug = False):

    return res_string


# #### _Exemple_ : __Projet Notation_scientifique__
# 
# Test de la fonction principale.

# In[5]:


# appel de la fonction


print ('X = ' + resultat_mesure)

