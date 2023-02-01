#!/usr/bin/env python
# coding: utf-8

# # Fonctions

# Un des enjeux de la programmation est la décomposition d'une procédure complexe en une cascade de sous-procédures de plus en plus simples.
# On appelle parfois ces sous-procédures des _routines_ du fait qu'elles sont tellement élémentaires que l'on fait régulièrement appelle à elles.
# 
# Par exemple :
# La procédure "__Se lever le matin__" peut se décomposer de la façon suivante :
# 
# - __definition__ de __Se lever le matin__ :
#     - __Initialiser__ le processeur
#     - heure_courante = __Lecture__ de l'affichage du réveil
#     - __Si__ heure_courante < heure_de_se_lever : __Ne rien faire__
#     - __Sinon__ : 
#     - __Si__ _soi_ est recouvert d'une couverture: 
#         - __Retrait__ de la couverture
#     - __Fin bloc si__
#     - __Se redresser__
#     - pied_a_bouger = __Identifier__ le pied le plus proche du bord du lit
#     - __Poser par terre__ pied_a_bouger 
#     - __Poser par terre__ ensemble_des_pieds - pied_a_bouger 
#     - __Contrôle de stabilité bipédique__
#     - __Atteindre la station bipédique__
#     - __Fin de la procédure__

# Chaque instruction peut être elle aussi une procédure ou une fonction. Par exemple :
# > __definition__ de __Lecture__ (chose_a_lire) :
# >> __Si__ les yeux sont fermés :__Ouvrir les yeux__\
# __Localisation__ de la position relative de chose_a_lire \
# heure_lue = __Lecture__ d'une chaîne de caractère au format "hh : mm"\
# __Retourne__ heure_lue\
# __Fin de la fonction__

# ### Arguments d'une procédure ou d'une fonction
# Ces procédures font intervenir des paramètres qui permettent de tenir compte du contexte d'exécution.
# Ces paramètres sont appelés les _arguments_ de la procédure.

# ### Procédure ou fonction ?
# _Remarque_ : certains langages de programmation distinguent les _fonctions_ des _procédures_ suivant qu'une variable est retournée ou non.  
# Python rassemble les deux sous le nom de _fonction_ et propose une type de variable vide pour marquer l'absence de valeur retournées par une _procédure_.
# - _Procédure_ : séquence d'instructions paramétrées par à des arguments et retournant une variable de type __None__.
# - _Fonction_ : séquence d'instructions paramétrées par à des arguments et retournant une ou plusieurs variable de tout type (sauf None).
# 

# Attention, un même programme peut être découpé de nombreuses façons différentes.
# C'est précisément dans cette décomposition que réside la valeur ajoutée de l'auteur·rice du programme.
# Les critères présidant à ces choix incluent 
# - la consommation en ressources (processeur, mémoire), 
# - le temps de développement, 
# - la lisibilité du code
# - le degré de modularité (partage, extension, ...) du code.

# ```python
# # Syntaxe Python d'une fonction
# def nom_de_la_fonction (argument1, argument2, argument3, ...) :
#     instruction1
#     instruction2
#     instruction3
#     ...
#     return output
# ```

# ### Première fonction, première procédure

# In[1]:


# première fonction
def incrementor (n):
    output = n+1
    return output

# première procédure
def printcoucou ():
    print ('Coucou')
    return None


# In[2]:


# Appel des fonctions et procédures

var = 11
new_var = incrementor (var)
print (new_var)
printcoucou ()


# Ces deux fonctions illustrent un principe important de la programmation :

# > <span style="color:red">__Ce n'est pas parce qu'une fonction renvoit un résultat qu'elle sert à quelque chose.__ </span>

# ### Variables locales ?

# Les variables d'une fonctions sont indépendantes des variables du programme appelant la fonction.
# Elle peuvent porter le même nom et rester distinctes.
# 
# <div class="alert alert-block alert-info">
# On qualifie ces variables de <b>locales</b> parce qu'elles sont détruites à la fin de l'exécution de la fonction.
# Seules les variables de sorties sont transmises au programme principal.
# 
# </div>

# In[3]:


def multiplicator (x1, x2) : # les variables de la fonction portent le même nom que dans le programme appelant
    x1 *= x2 #la variable locale x1 est modifiée
    return x1

x1 = 2
x2 = 3
x3 = multiplicator (x1, x2) 
print ('x1 =', x1) # la variable x1 n'est pas modifiée par l'exécution de la fonction
print ('x3 =', x3)


# Il en va de même pour les tuples qui sont des conteneurs non modifiables.

# In[4]:


def concatenator (x1, x2) :
    x1 += x2 #la variable locale x1 est modifiée
    return x1

x1 = (1, 2, 3)
x2 = (4, 5, 6)
x3 = concatenator (x1, x2)
print ('x1 =', x1)
print ('x3 =', x3)


# Lorsque des conteneurs modifiables comme des listes ou des dictionnaires sont passées en argument d'une fonction, elles ne sont pas dupliquées lors de l'exécution de la fonction.
# Par conséquent, les modifications dans une fonction sont conservées dans le programme principale.

# In[5]:


x1 = [1, 2, 3]
x2 = [4, 5, 6]
x3 = concatenator (x1, x2)
print ('x1 =: ', x1)
print ('x3: ', x3)


# <span style="color:red">Syntaxe risquée</span>

# In[6]:


def dictionary_merger (x1, x2):
    x1 |= x2
    return x1

x1 = {'janvier': 31, 'fevrier': 28, 'mars': 31, 'avril': 30}
x2 = {'mai': 31, 'juin': 30, 'juillet': 31, 'aout': 31, 'fevrier': 29}
x3 = dictionary_merger (x1, x2)
print(x1)
print(x3)


# <span style="color:green">Syntaxe sure</span> (créer une nouvelle variable dans la fonction)

# In[7]:


def dictionary_merger (x1, x2):
    output = x1 | x2
    return output

x1 = {'janvier': 31, 'fevrier': 28, 'mars': 31, 'avril': 30}
x2 = {'mai': 31, 'juin': 30, 'juillet': 31, 'aout': 31, 'fevrier': 29}
x3 = dictionary_merger (x1, x2)
print(x1)
print(x3)


# La fonction suivante illustre les inconvénients susceptibles de survenir en cas de modification d'une liste dans une fonction.

# In[8]:


def index_of_elem_in_list (liste, elem):
    N = len(liste)
    if elem not in liste:
        output = -1
    else:
        output = ()
        i = 0
        for i in range (N):
            if liste[0] == elem:
                output += (i,)
            liste.pop(0)
            # print (f'itération {i:d} : ', liste) # décommenter pour voir afficher l'état de la liste à chaque itération
    return output

X = [1, 2, 8, 4, 5, 6, 7, 8, 9]
elem = 8
print ('etat de la liste X avant appel de la fonction:\n', X)
print (f'Indice·s de {elem:d} dans X : {index_of_elem_in_list (X, elem)}')
print ('Etat de la liste X après appel de la fonction:\n', X)

