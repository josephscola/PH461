#!/usr/bin/env python
# coding: utf-8

# # Méthodologie de la programmation en C, A. Braquelaire
# 
# Notes sur le chapitre 8 : modulariasation des programmes C
#     
# ## Objectifs de la modularité :
# A. Braquelaire définit les cinq objectifs suivants :
# 1. __Lisibilité__ : facilité à comprendre le comportement et la mise en œuvre d'un programme à partir de son code source.
# 2. __Maintenabilité__ : facilité à détecter des fautes de programmation et à les corriger sans en introduire de nouvelles.
# 3. __Portabilité__ : facilité à adapter toutes les fonctionnalités d'un logiciel à un nouvel environnement.
# 4. __Extensibilité__ : ossibilité de modifier l'implémentation d'une partie du programme ou de lui ajouter des fonctionnalités sans que cela ne modilie le comportement de l'ensemble.
# 5. __Réutilisabilité__ : possibilité d'assembler entre eux plusieurs portions de programme, écrites à des époques et pour des applications différentes, sans qu'aucune d'entre elles ne perturbe le comportement des autres.
# 
# Il s'agit donc de regrouper les fonctionnalités concourrant à un même traitement.
# Il existe 2 approches de regroupement qui s'opposent
# - "dirigée par le contrôle" : approche fonctionnelle "descendante incompatibie avec la réutilisabilité et l'extensibilité
# - "dirigée par les données" : approche ascendante favorable à la construction de composants logiciels autonomes (voir prog. par objet).
# 
# Si on décline  ces approches dans le contexte du PH461 qui vise au développement d'outils d'analyse de données expérimentales, apparaissent les options suivantes.
# Partant du constat que des données doivent être lues, traitées puis représentées graphiquement,
# la _méthode descendante_ consisterait à développer des fonctions de représentation pour chaque type de données en incluant les traitements associés aux différents cas de figure.
# Ainsi, les $X(t)$ d'une acquisition temporelle pourraient très bien se trouvées dans un format différent (une liste par exemple) de celles d'une acquisition en fonction de la température $X(T)$ (qui aurait le type d'un dictionnaire).
# Cela rendrait nécessaire d'écrire deux versions des fonctions de traitements et de représentation alors même que les opérations seraient communes à n'importe quelle fonction d'une seule variable $f(x)$.
# A l'inverse la _méthode ascendante_ impliquerait de commencer par développer pour chaque origine de données (et donc chaque format de fichier de données) une fonction qui chargerait les données en mémoire dans un format particulier et toutes les fonctions de traitement seraient compatibles avec ce format (par exemple des listes).

# ## Principes fondamentaux de la modularité
# 
# ### 1. "Abstraction des littéraux"
# Toute grandeur constante dans un programme donné est susceptible de prendre une autre valeur dans une réutilisation future. 
# L'_abstraction des littéraux_ consiste à déclarer une variable pour toutes les constantes d'un programme.
# - exemple 1
# 
# <span style="color:red">mauvaise pratique :</span>
# <code> <pre> annee_complete = 1900 + annee </pre></code>
# <span style="color:green">bonne pratique :</span>
# <code> <pre>annee0 = 1900
# annee_complete = 1900 + annee </pre></code>
# - exemple 2
# 
# <span style="color:red">mauvaise pratique :</span>
# <code> <pre> open ('/home/mon_repertoire/mon_fichier.dat') </pre></code>
# <span style="color:green">bonne pratique :</span>
# <code><pre>path = '/home/mon_repertoire/'
# file = 'mon_fichier.dat' 
# open (path + file)</pre></code>
# 
# ### 2. "Facorisation du code"
# Le but est d'éviter les duplications de code qui entrave la _maintenabilité_ et l'_extensibilité_ puisque les corrections et les adaptations doivent être autant dupliquées que le code se trouve l'être.
# 
# 

# #### Exemple 1 : représentation d'un nombre complexe 
# On souhaite afficher un nombre complexe sous sa forme cartésiène :
# $$ z =  1 + 2i $$ 

# In[1]:


z = 1+2j
print (f'{np.real(z):.1f} + {np.imag(z):.1f}i')


# Imaginons que dans un autre contexte, il soit nécessaire de remplacer le symbole $i$ du nombre imaginaire par $j$, il faudrait modifier toutes les instructions d'affichage.
# Pour éviter cela, la chaîne de caractère à afficher doit être définie dans une fonction.

# In[105]:


def affiche_complexe (z, symbol):
    return f'{np.real(z):.1f} + {np.imag(z):.1f}' + symbol
print (affiche_complexe (1+2j, 'i'))
print (affiche_complexe (1+2j, 'j'))
print (affiche_complexe (1+2j, '◎'))


# <blockcquote>On considérera qu'il y a duplication de code chaque fois qu'une modifiation doit être répercuytée en plusieurs endroits différents du programme. Les fonctions doivent être systématiquement employées pour éviter la duplication de code, même dans le cas où la duplucation se limite à une seule instruction. Si cela s'avère nécessaire, il ne faut pas craidre de définir une multitude de fonctions de petite tailles.</blockcquote>

# #### Exemple 2 : représentation d'un résultat de mesure
# Le résultat d'une expérience se représente dans la notation scientifique et associe la valeur moyenne de la mesure, l'incertitude de mesure et l'unité de la grandeur mesurée :
# $$ X = (1.234 \pm 0.056)\cdot 10 ^{-6} \quad \mathrm{m}$$

# In[29]:


# données expérimentales
X = 1.234e-6
Delta_X = 0.056e-6
unit = 'm'

# affichage du résultat de mesure 
exp = -6
odg = 10**exp
print (f'X = ({X/odg:.3f} ± {Delta_X/odg:.3f}) 10^({exp:d}) ' + unit)


# Cette manière de faire est fonctionnelle mais ne respecte pas les principes de modularité.
# Si dans un usage ultérieur, on souhaitait représenter un résultat ayant un chiffre significatif supplémentaire : 
# $$ Y = (1.2345 \pm 0.0056)\cdot 10 ^{-6} \quad \mathrm{m},$$
# il serait nécessaire de dupliquer le code et de modifier le format d'affichage des variables réelles, en plus du nom de la grandeur.

# In[31]:


# données expérimentales
Y = 1.2345e-6
Delta_Y = 0.0056e-6
unit = 'm'

# affichage du résultat de mesure 
exp = -6
odg = 10**exp
print (f'Y = ({Y/odg:.4f} ± {Delta_Y/odg:.4f}) 10^({exp:d}) ' + unit)


# Pour éviter cela, et rendre possible l'application du code pour des contextes variés, la décomposition du travail en fonctions et sous-fonctions est nécessaire.

# In[95]:


import numpy as np

def ordre_de_grandeur (x):
    # retourne l'ordre de grandeur de x
    return int (np.round (np.log10 (x)))

def ordre_de_l_erreur (err, debug = False):    
    # recherche l'ordre de grandeur du plus petit chiffre significatif de l'erreur
    odgerr = 0
    while (err > np.floor (err)) :
        err = err * 10
        odgerr -= 1
        if debug : print ('err = ', err)
        if debug : print ('odgerr = ', odgerr)
    return odgerr

def represente_resultat_mesure (val, err, unit, debug = False):
    odg = ordre_de_grandeur (val)
    if debug: print ('odg = ', odg)
    odgerr = ordre_de_l_erreur (err)
    if debug: print ('odgerr = ', odgerr)
    nb_de_decimales = odg - odgerr
    if debug: print (nb_de_decimales)
    val_string = f'{val / 10**odg:.{nb_de_decimales}f}'
    err_string = f'{err / 10**odg:.{nb_de_decimales}f}'
    res_string = '(' + val_string + ' ± ' + err_string + f')⋅1e{odg:d} ' + unit
    return res_string

# Script appelant les fonctions
val = 1.123456e-6
err = 0.0056e-6
resultat_mesure = represente_resultat_mesure (val, err, 'm')
print ('X = ' + resultat_mesure)

