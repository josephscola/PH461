#!/usr/bin/env python
# coding: utf-8

# # Types de variables

# Il est souvent nécessaire de rassembler plusieurs variables au sein d'un même objet.
# 
# qu'on appelle conteneur (_containers_ en anglais).
# Par exemple, la _chaîne de caractères_ rassemble une séquence ordonnée de caractères qu'il est commode de manipuler comme un objet à par entière.
# Chaque élément dans un conteneur est accessible par son indice, c'est-à-dire le rang dans la séquence.
# 

# ## Différentes structures de données en Python
# Il est souvent nécessaire de rassembler plusieurs variables au sein d'un même objet (par exemple les coordonnées GPS d'un lieu ou les éléments d'une matrice).
# 
# Les types de structures de données sont :
# - les conteneurs (les éléments y sont accessibles par un indice) :
#     - non modifiables :
#         - __les chaînes de caractères__ (les éléments sont des symboles [ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange))
#         - les __t-uples__ (les éléments sont de tous types)
#     - modifiables :
#         - les __listes__ (t-uples modifiables après initialisation)      
# - les __dictionnaires__ : les éléments y sont accessibles par un mot-clé.
# - les __classes__ : le type des éléments y est prédéfini et des opérations sur les éléments peuvent être incluses (par exemple on peut définir la classe des nombres complexes dont les variables sont la partie réelle et la partie imaginaire du nombre auxquelles on associe les opérations de calcul du module et de l'argument, ...).
# Les classes ne seront pas abordées dans ce cours mais pourront être employées, le cas échéant, dans les projets numériques.

# ## Les conteneurs : 
# Un conteneur (de _container_ en anglais) est une séquence ordonnée rassemblant des éléments d'un même type ou de types différents; on accède aux éléments d'un conteneur par son _indice_, c'est-à-dire son rang dans la séquence.
# > <span style="color:red">__ATTENTION ! Les indices sont numérotés à partir de 0.__ </span>
# #### Syntaxes communes à tous les conteneurs
# La surcharge de l'opérateur (__+__) pour la concaténation est valable pour tous les types de conteneur.
# De même la fonction __len ()__ s'applique à n'importe quel type de conteneur.
# 
# 

# ## Les listes  : conteneurs modifiables
# 

# ### Déclaration explicite d'une liste 

# In[1]:


ma_premiere_liste = [1, 2, 3, 4, 5]
print (ma_premiere_liste)

ma_deuxieme_liste = ['un', 'deux', 'trois', 'quatre', 'cinq']
print (ma_deuxieme_liste)

ma_troisieme_liste = ['un', 2, 3.0, [4, 'cinq']]
print (ma_troisieme_liste)
print ('Le nombre d\'éléments dans ma_troisieme_liste est : ', len (ma_troisieme_liste))


# ### Déclaration récursive et ajout d'un élément à une liste
# L'ajout d'un élément à la fin d'une liste se fait par simple _concaténation_.

# In[2]:


x = [] # création d'une liste vide
x += [1]
x += [2]
print (x)


# ### Accès aux éléments d'une liste

# In[3]:


ma_deuxieme_liste = ['un', 'deux', 'trois', 'quatre']


# ### Accès par l'indice

# In[4]:


print (ma_deuxieme_liste [1])


# ### Accès par tranche

# In[5]:


print (ma_deuxieme_liste [0:2])


# ### Accès à partir de

# In[6]:


print (ma_deuxieme_liste [1:])


# ### Accès jusqu'à

# In[7]:


print (ma_deuxieme_liste [:3])


# ### Accès par le rang en partant de la fin

# In[8]:


print (ma_deuxieme_liste [-1])


# In[9]:


print (ma_deuxieme_liste [-2])


# ## Méthodes ("fonctions intégrées") associées aux listes

# ### .index ()
# La méthode __.index ()__ retourne l'indice d'un élément passé en argument de la méthode.

# In[10]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
indice = x.index (8)
print ("L'indice de 8 dans x est ", indice)


# ### .remove ()
# La méthode __.remove ()__ retire l'élément passé en argument (Attention : méthode hautement dangereuse)

# In[11]:


x = [1, 2, 3, 4, 5, 6, 7, 8]
VALEUR_RETOURNEE_DE_REMOVE = x.remove (7)
print ("Après le retrait de 7, il ne reste dans x que ", x)
print (VALEUR_RETOURNEE_DE_REMOVE)
x += [7]
print ("après réintégration de 7, x contient : ", x)


# print (VALEUR_RETOURNEE_DE_REMOVE)#### Test d'appartenance

# In[12]:


ma_liste = ['un', 'deux', 'trois', 'quatre', 'cinq']
test1 = 'deux' in ma_liste
print ('deux est dans ma_liste : ', test1)
test2 = 'six' in ma_liste
print ('six est dans ma_liste : ', test2)


# ### Fonction __zip ()__

# In[13]:


x = [1, 2, 3, 4]
y = [3, 6, 9, 12]
z = [5, 10, 15, 20]
data = [x, y, z]
noms = ['abscisse', 'ordonnées']
zipped_list = zip (noms, data)
print (list (zipped_list))


# ### Copie d'une liste
# A la différence des variables numériques ou des chaînes de caractères pour lesquelles un espace mémoire est associé de manière univoque à l'identifiant de la variable, l'identifiant d'une liste (son nom dans le programme) ne contient que l'adresse de l'espace mémoire alloué, mais pas à son contenu.
# Il en résulte que la copie par création d'une nouvelle liste égale à la première n'a pour résultat que la création d'un nouveau nom pour le même espace mémoire.

# In[14]:


x = ['je', 'suis', 'unique' ]
y = x
print ('Avant la modification de x, y == x : ', y==x)
x += ['et', 'ne', 'me', 'laisserai', 'pas', 'dissocier', 'de', 'mes', 'copies']

print ('Après la modification de x, y == x : ', y==x)
print('la liste copiée y contient : \n', y)


# Pour créer une copie véritablement indépendante de la liste originale, il faut la copier élément par élément dans une nouvelle liste.

# ## Conteneurs non modifiables : t-uples
# On utilise les t-uples à chaque fois que l'on veut être certain que les données transmies ne seront pas modifiées par erreur au sein du programme.

# In[15]:


x = (1, 2, 3)
y = (4, 5, x)
print ('y' + ' '*8+'= ', y)
print ('y [2]'+ ' '*4+'= ', y [2])
print ('y [2][0] = ', y [2][0])


# In[16]:


x = (1, 2, 3)
print (type (x))


# L'ajout d'un élément à un t-uple existant se fait par l'opérateur __+__ :

# In[17]:


x = (1, 2, 3)
x = x + (4,)
x = x + (5.,)
x = x + ('toto',)
print ('x = ', x)


# ### Empaquetage et désempaquetage d'un t-uple
# Les t-uples sont particulièrement commodes pour rendre plus lisible la lecture d'un code grâce à leurs possibilités d'empaquetage et de désempaquetage.
# Ces opérations permettent d'affecter plusieurs variables en une seule ligne.

# In[18]:


coordonnees_de_v = 1., 2, 0.
print (coordonnees_de_v)
x, y, z = coordonnees_de_v
print (x)
print (y)
print (z)


# ### Modification d'un  t-uple
# La modification d'un t-uple n'est pas permise.

# In[19]:


x = 1, 2, 3
x [0] = '12' # la modification d'un t-uple n'est pas permise
print (x)


# In[32]:


print (x)
y = list (x)
y [0] = '12'
print ('y = ', y)


# ### Les parenthèses ne sont pas indispensables pour définir un t-uple

# In[33]:


avec = (1, 2, 3) 
sans = 1, 2, 3
expression = ( avec == sans )
print (expression)


# ## Tuple ou liste ?
# Les tuple et les listes offrent les mêmes fonctionnalités de stockage d'un ensemble de variables de divers types avec accès par l'indice du rang de stockage.
# A l'usage, ces deux types de conteneurs présentent différences suivantes.

# ### 1. argument de fonction:
# Le tuple est dupliqué localement dans la fonction, la liste ne l'est pas. Les listent présentent donc l'inconvénient des variables globales : toute modification d'une liste dans une fonction est implicitement répercutée dans le programme principale (avantage tuple)

# In[3]:


def indice_de_elem_dans_conteneur (elem, conteneur):
    sortie = str(elem) + ' ne se trouve pas dans ' + str(conteneur)
    i = 0
    while len(conteneur) > 0 and type(sortie) == str:
        if conteneur[0] == elem:
            sortie = i
        else:
            conteneur = conteneur [1:] # retire le premier élément du conteneur
            i += 1
    conteneur += conteneur
    return conteneur


# In[4]:


mon_tuple = (1, 2, 3, 'quatre', 5, 6)
ma_liste = [1, 2, 3, 'quatre', 5, 6]

elem = 'quatre'
indice_de_elem_dans_conteneur (elem, ma_liste)
indice_de_elem_dans_conteneur (elem, mon_tuple)

mon_tuple
ma_liste


# ### 2. protection des éléments
# Les éléments d'un tuple sont protégés : leur modification nécessite la création d'un nouveau conteneur. La rigidité caractéristique des tuple complique (un peu) le codage, mais simplifie (beaucoup) la recherche d'erreurs et l'extension des programme (avantage tuple)
# 

# ### 3. affectation-concaténation de chaînes de caractères :
# L'affectation-concaténation est possible pour les listes et pour les tuples, mais ne produit pas le même résultat lorsque la variable affectée-concaténée est une chaîne de caractère : les caractères de la chaîne se trouvent distribués en éléments séparés dans le cas de la liste.

# In[1]:


mon_tuple = (1, 2, 3)
mon_tuple += ('cinq',)
print (mon_tuple)

ma_liste = [1, 2, 3, 4]
ma_liste += 'cinq'
print (ma_liste)

ma_liste.append ('six')
print (ma_liste)


# ### 3. méthodes natives:
# Les méthodes associées aux listes sont plus nombreuses et puissantes que celles des tuples (avantage liste)

# In[ ]:





# In[ ]:


mon_tuple = (1, 2, 3)
mon_tuple += ('cinq',)
print (mon_tuple)

ma_liste = [1, 2, 3, 4]
ma_liste += 'cinq'
print (ma_liste)

ma_liste.append ('six')
print (ma_liste)


# ## Dictionnaires
# A la différence des t-uple et des listes dans lesquels l'accès direct aux éléments se fait par un indice (donné entre crochets), l'accès aux éléments d'un dictionnaire se fait par _mots clef_ (de type __str__).

# In[10]:


# exemple de dictionnaire
jours_dans_le_mois = {'janvier' : 31,
                      'février' : (28,  29),
                      'mars' : 31,
                      'avril' : 30,
                      'mai' : 31,
                      'juin' : 30,
                      'juillet' : 31,
                      'aout' : 31,
                      'septembre' : 30,
                      'octobre' : 31,
                      'novembre' : 30}
print ('Le contenu du dictionnaire est :\n', jours_dans_le_mois)
print (type (jours_dans_le_mois))


# In[2]:


mois = 'janvier'
print (f'Il y a {jours_dans_le_mois [mois]:d} jous dans le mois de', mois)


# ### Ajout d'un élément à un dictionnaire

# In[3]:


jours_dans_le_mois ['décembre'] = 31
print ('Le nouveau contenu du dictionnaire est :\n', jours_dans_le_mois)


# ### Méthode .keys ()
# La méthode __.keys ()__ retourne l'ensemble des _mots-clef_ du dictionnaire.

# In[4]:


print ('Les entrées du dictionnaire sont :')
print (jours_dans_le_mois.keys ())


# ### Méthode .items ()
# La méthode __.items ()__

# In[5]:


jours_dans_le_mois.items ()


# ### Comment utiliser les dictionnaires ?
# Les dictionnaires offrent un outil puissant pour construire des bases de données évolutives constituées de dictionnaires en cascade.
# Dans le contexte particulier de l'analyse de données en Physique, ils peuvent être utilisés efficacement dans le référencement de jeux de données expérimentales et de leurs résultats d'analyse
# 
# <div class="alert alert-block alert-info"> <b> 1 fichier de données = 1 entrée du dictionnaire </b></div>

# ## Fonction len()
# La fonction __len__ permet de connaître la longueur de n'importe quel type de conteneur.

# In[13]:


# renvoie le nombre d'entrées d'un dictionnaire
len (jours_dans_le_mois)


# In[17]:


# renvoie le nombre d'éléments d'un tuple ou d'une liste
len (['1', '2', '3', ['quatre', 'cinq', 'six']])


# In[16]:


# renvoie le nombre d'éléments d'un tuple
mon_tuple = (1, 2, 3, 4, 5), (6, 7, 8, 9, 10)
len (mon_tuple)

