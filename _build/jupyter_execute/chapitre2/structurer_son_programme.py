#!/usr/bin/env python
# coding: utf-8

# # Structurer son programme
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
    # retourne l'ordre de grandeur de x
    res = 1
    if x != 0 :
        res = int (np.floor (np.log10 (np.abs(x))))
    return res

def ordre_de_l_erreur (err, debug = False):    
    # retourne l'ordre de grandeur du plus petit chiffre significatif de l'erreur
    # err : valeur numérique de l'incertitude expérimentale
    odgerr = 0
    while (err > np.floor (err)) :
        err = err * 10 
        # modification ici de l'argument d'entrée mais c'est un float donc la variable originale est protégée
        odgerr -= 1
        if debug : print ('err = ', err) # contrôles du déroulement de la boucle : 
        if debug : print ('odgerr = ', odgerr)
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
valeurs = (1e-180, 0., 9.9999e180)
for valeur in valeurs :
    print (ordre_de_grandeur (valeur))


# In[3]:


# test de ordre_de_l_erreur
erreurs = (0.1, 0.12, 0.123, 0.1234)
for erreur in erreurs :
    print (ordre_de_l_erreur (erreur))


# _Exemple_ : __Projet Notation_scientifique__
# 
# Fonction principale appelant les sous-fonctions.

# In[4]:


# fonction erronée
def represente_resultat_mesure_ (val, err, unit, debug = False):
    # identifie l'ordre de grandeur de l'erreur comme celui de son plus petit chiffre significatif
    # retourne une chaine de caractère au format notation scientifique
    odg = ordre_de_grandeur (val)
    if debug: print ('odg = ', odg)
    odgerr = ordre_de_l_erreur (err, debug)
    if debug: print ('odgerr = ', odgerr)
    nb_de_decimales = odg - odgerr
    if debug: print ('nombre de décimales : ', nb_de_decimales)
    val_string = f'{val / 10**odg:.{nb_de_decimales}f}'
    err_string = f'{err / 10**odg:.{nb_de_decimales}f}'
    res_string = '(' + val_string + ' ± ' + err_string + f')⋅1e{odg:d} ' + unit
    return res_string


# In[5]:


# debugged function
def represente_resultat_mesure (val, err, unit, debug = False):
    # identifie l'ordre de grandeur de l'erreur comme celui de son plus petit chiffre significatif
    # retourne une chaine de caractère au format notation scientifique
    res_string = '' # valeur par défaut, retourné en cas d'erreur ou d'exception
    odg = ordre_de_grandeur (val)
    if debug: print ('odg = ', odg)
    odgerr = ordre_de_l_erreur (err, debug)
    if debug: print ('odgerr = ', odgerr)
    nb_de_decimales = odg - odgerr
    if debug: print ('nombre de décimales : ', nb_de_decimales)
    if nb_de_decimales >= 0 : 
        val_string = f'{val / 10**odg:.{nb_de_decimales}f}'
        err_string = f'{err / 10**odg:.{nb_de_decimales}f}'
        res_string = '(' + val_string + ' ± ' + err_string + f')⋅1e{odg:d} ' + unit
    else :
        print ('ERREUR : la valeur mesurée est négligeable devant l\'incertiude')
    return res_string


# #### _Exemple_ : __Projet Notation_scientifique__
# 
# Test de la fonction principale.

# In[6]:


# appel de la fonction
val = 9.123456e-6
err = 0.0056e-6
unit = 'm'

resultat_mesure = represente_resultat_mesure (val, err, unit)
print ('X = ' + resultat_mesure)


# In[7]:


# Test du programme avec plusieurs configurations
variables_test  = ()
variables_test += (9.123456e-6, 0.0056e-6, 'm'), 
variables_test += (1.123456e-6, 0.0056e-6, 'm'), 
variables_test += (0.123456e-6, 0.0056e-6, 'm'),
variables_test += (0.123456e-6, 0.00564e-6, 'm'),
variables_test += (0.123456e-10, 0.0056e-6, 'm'),

for variable_test in variables_test :
    val, err, unit = variable_test
    resultat_mesure = represente_resultat_mesure (val, err, unit)
    print ('X = ' + resultat_mesure)

