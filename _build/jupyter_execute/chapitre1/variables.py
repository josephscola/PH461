#!/usr/bin/env python
# coding: utf-8

# # Variables numériques

# ## Qu'est-ce qu'un variable ?

# Une variable est à la fois un _identifiant_ dans le programme (un nom de variable) associée à une _zone de la mémoire_ de l'ordinateur dans laquelle est affecté la _valeur_ ou les _valeurs_ successives affectées à la variable.
# Avant d'être utilisée, une variable doit être déclarée et initialisée.
#    1. La déclaration d'une variable est la définition son type; cela conditionne les valeurs qu'elle peut recevoir, les opération qu'on peut lui appliquer ainsi que l'espace mémoire qui lui est alloué.
#    2. L'initialisation d'une variable consiste à lui attribuer une valeur particulière avant sa première intervention dans le programme.
# 
# En Python, la déclaration est faite implicitement au moment de l'initialisation : le type de la variable est celui de la valeur qui lui est affectée.
# C'est pratique, mais expose au risque de confusion quant au type des variables.

# ## Entiers machine

# La représentation machine des _entiers_ est faite par un _mot_ binaire : chaque bit prend la valeur 1 ou 0 qui multiplie la puissance de 2 associée à son rang dans le _mot_.
# 
# $$ 
# (10010100)_2 = 1\cdot 2^7 + 
#                0\cdot 2^6 +  
#                0\cdot 2^5 + 
#                1\cdot 2^4 + 
#                0\cdot 2^3 + 
#                1\cdot 2^2 + 
#                0\cdot 2^1 + 
#                0\cdot 2^0
#              = 148
# $$
# 
# Il existe plusieurs types d'entiers machine.
# Suivant que l'on souhaite représenter des valeurs plus ou moins grandes, on modifiera la longueur du mot : 
# le plus grand entier machine codé sur $N$ bits est $2^N - 1$.

# In[1]:


x = 2**7
print ('2**7 + 1 = ', x+1)
print('le type de x est : ', type (x))
print ('le nombre d\'octets alloué à x est : ', x.__sizeof__()) #


# In[2]:


x = 2**127
print ('2**127 + 1 = ', x+1) # l'ancienne valeur est écrasée
print('le type de x est : ', type (x)) # la variable x a été remplacée par une autre du même type
print ('le nombre d\'octets alloué à x est : ', x.__sizeof__()) # la nouvelle varable occupe plus de mémoire


# Python ajuste automatiquement la longueur du _mot_ binaire en fonction du nombre à représenter.

# Pour une longueur de mot, on distingue deux types d'entiers suivant que le _bit de poids fort_ ($2^7$ pour le mot de 8 bits de l'exemple) est remplacé ou non par un _bit de signe_.
# $$ 
# (10010100)_2 = (-1)^1 \times (
#                0\cdot 2^6 +  
#                0\cdot 2^5 + 
#                1\cdot 2^4 + 
#                0\cdot 2^3 + 
#                1\cdot 2^2 + 
#                0\cdot 2^1 + 
#                0\cdot 2^0)
#              = -20
# $$

# ## Réels machine

# La représentation des réels comme une partie entière séparée d'une décimale par une virgule n'est pas adapté à la représentation par une machine.
# Une des raisons est que l'espace mémoire nécessaire ne dépend plus seulement de la valeur numérique mais également de sa précision.
# En pratique, les réels sont représentés par trois entiers :
# - le _bit de signe_ $s$,
# - un entier non signé _mantisse_ $m$,
# - un entier signé (ou relatif) l'_exposant_ $n$.
# Tout _réel machine_ $x$ est représenté par $$ x = (-1)^s \cdot m\cdot 10^n $$

# In[3]:


y = 2.
print ('2. = ', y)
print ('le nombre d\'octets allouées à y est : ', y.__sizeof__())

y1 = 2.000000000000001
print ('y1 - y = ', y1 - y)
print ('le nombre d\'octets allouées à y est : ', y1.__sizeof__())

y2 = 2.0000000000000001
print ('y2 - y = ', y2 - y)
print ('le nombre d\'octets allouées à y est : ', y2.__sizeof__())


# <span style="color:red"> <b> ATTENTION : les réels démunis de représentations machine sont ARRONDIS !!! </b></span>

# <div class="alert alert-block alert-info"> <b> REGLE A SUIVRE : normaliser les valeurs numériques pour que les calculs soient faits autour de 1 </b></div>

# In[4]:


a, b, c = 1., 2., 1 
while c < 18 : 
     a, b, c = b, b * a, c + 1 
     print (f'itération {c:2d} : b = {b:22}; (allocation mémoire : {b.__sizeof__():d} octets)')  


# Lorsque la capacité de la représentation en virgule flottante est dépassée ($\pm 10^{\pm 308}, avec 16 chiffres significatifs), les valeurs numériques sont remplacées par l'_infini machine_ (__inf__)

# ## Opérations sur les variables numériques

# #### Addition (+), soustraction (-)

# In[5]:


x = 2
y = 2.
z = x - y
print ('2 - 2. = ', z)
print ('le type de z = (x - y) est : ', type (z))


# #### Multiplication (*), division (/)

# In[6]:


x = 2
y = 2.
z = x * y
print ('2 * 2. = ', z)
print ('le type de z = (x * y) est : ', type (z))


# In[7]:


x = 2
y = 2.
z = x / y
print ('2 / 2. = ', z)
print ('le type de z = (x / y) est : ', type (z))


# #### Puissance (**)

# In[8]:


x = 2
y = 0.5
z = x ** y
print ('2 ** 0.5 = ', z)
print ('le type de z = (x ** y) est : ', type (z))


# #### Division entière (//)

# In[9]:


x = 11
y = 2
z = x // y
print (z)


# #### Reste de la division entière (%)

# In[10]:


x = 11
y = 2
z = x % y
print (z)


# #### Combinaisons opération-affectation (+=, -=, *=, /=)

# In[11]:


x = 2
print ('avant addition-affectation, x = ', x)
x += 2 # équivalent à x = x + 2
print ('après addition-affectation, x = ', x)

x = 3
print ('avant soustraction-affectation, x = ', x)
x -= 2 # équivalent à x = x + 2
print ('après soustraction-affectation, x = ', x)


# ### Conversion de type

# #### Conversion __int__ &rarr; __float__
# La conversion d'une variable de type __int__ en un réel de type __float__ se produit sans modification de la valeur numérique initiale.

# In[12]:


x = 2
print ('après initialisation à 2')
print ('x = ', x)
print ('le type de x est : ', type (x))

x = float (x)
print ('après conversion en réel à virgule flottante')
print ('x = ', x)
print ('le type de x est : ', type (x))


# #### Conversion __float__ &rarr; __int__
# La conversion d'une variable en virgule flottante s'accompagne de la troncature de la partice décimale du réel.

# In[13]:


x = 2.9
print ('après initialisation à 2.9')
print ('x = ', x)
print ('le type de x est : ', type (x))

x = int (x)
print ('après conversion en entier')
print ('x = ', x)
print ('le type de x est : ', type (x))


# ## Nommage des variables

# #### Noms réservés
# | | | | | | | | |
# |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
# |and |	as	|assert |	break	|class	|continue|	def|del|
# |elif|	else|	except	|exec |	finally|	for	|from	|global|
# |if|	import|	in	|is	|lambda	|not	|or|	pass|
# |print |	raise	|return	|try	|while|	with	|yield|
# 
# La plupart des éditeurs (dont notebook) reconnaissent ces mots et les rendent identifiables en leur donnant une couleur particulière.
# 
# #### Caractères spéciaux
# La plupart des caractères spéciaux (ponctuation, tirets, ...) ont une signification pour l'interpréteur Python3. Par conséquent, leur usage dans les nom de variable est interdit.
# Exception importante :
# > <span style="color:red">__L'emploi du caractère "souligné" ('\_') est fortement recommandé pour la lisibilité des variables__ </span>

# In[14]:


variable_facile_a_lire = 20/20
variableinutilementillisible = 0/20


# #### Majuscule et minuscules
# L'interpréteur Python3 tient compte de la casse dans le nom des variables

# In[15]:


toto = 13
print (Toto)


# #### Caractères linguistiques
# Les caractères spécifiques à certaines langues mais absente de l'anglais sont permises par l'interpréteur Python3 mais sont à éviter; en cas de partage, elles sont susceptibles de créer des problèmes d'incompatibilité (encodage des fichiers textes).

# In[9]:


toté = 2
print (toté)


# #### Usage "ancestral"
# Si le nom d'une variable ne comporte qu'une seule lettre latine, on associe traditionnellement :
# - un entier aux lettres $i$, $j$, $k$, $m$, et $n$
# - un réel pour les autres lettres.
# 
# #### Ni o ni O
# Pour des raisons de lisibilité évidentes, on évite de nommer une variable $o$ ou $O$.
