#!/usr/bin/env python
# coding: utf-8

# # Flux d'instructions
# L'ordre dans lequel les instructions sont exécutées s'appelle le flux d'instruction.
# Il existe trois modes de contrôle du flux des instructions :
# - la [séquence](#sequence) : exécution des instructions les unes après les autres
# - la [sélection](#selection) : instruction conditionnelle d'une séquence d'instructions
# - la [répétition](#repetition) : exécution en boucle d'une séquence jusqu'à réalisation d'un critère de sortie

# ## Séquence <a class="anchor" id="sequence"></a>

# Sauf instruction spécifique, les instructions d'un programme sont exécutées de façon séquentielle, les unes après les autres.

# Exemple d'une séquence d'instructions :
# > __se lever__ tôt le lundi\
# __prendre__ le petit-déjeuner le lundi \
# __se lever__ tôt la mardi\
# __prendre__ le petit-déjeuner le mardi \
# __se lever__ tôt le mercredi\
# __prendre__ le petit-déjeuner le mercredi\
# __se lever__ tôt le jeudi\
# __prendre__ le petit-déjeuner le jeudi \
# __se lever__ tôt le vendredi\
# __prendre__ le petit-déjeuner le vendredi \
# __se lever__ tôt le samedi\
# __prendre__ le petit-déjeuner le samedi \
# __se lever__ moins tôt le dimanche\
# __prendre__ le déjeuner le dimanche

# ```python
# ### syntaxe Python d'une séquence d'instructions
# instruction1
# instruction2
# instruction3
# ...
# ```

# ## Répétition <a class="anchor" id="repetition"></a>

# Il existent deux type de boucles de répétition suivant que les instructions sont répétées un nombre de fois prédéfini ou bien qu'un critère d'arrêt de la répétition a été  défini avant de la commencer.
# 
# ### Boucle for
# Les instructions incluses dans une boucles __for__ sont répétées un nombre de fois défini.
# Par exemple :
# 
# >__Pour__ chaque jour du lundi au samedi :
# >> __se lever__ tôt le matin \
# __prendre__ le petit déjeuner\
# __Fin de la boucle for__
# 
# >__se lever__ moins tôt et prendre le déjeuner le dimanche

# ```python
# # syntaxe Python d'une boucle for
# for element in objet_denombrable :
#     instruction1
#     instruction2
#     instruction3 ...
# ```

# > <span style="color:red">__Les instruction devant être répétées sont définies par l'indentation__ </span>

# In[1]:


# exemple minimal de boucle for
print ('bonjour')
for chiffre in 1, 2, 3, 4 :
    print (chiffre)
print ('au revoir')


# In[2]:


# exemple de boucles for imbriquées
# la seconde boucle est l'instruction unique de la première -> une tabulation
# les instructions de la seconde boucle sont indentées par rapport à la première -> deux taulations
print ('bonjour')
for chiffre in 1, 2, 3, 4:
    for lettre in 'a', 'b', 'c', 'd' :
        print (chiffre, lettre)
        print ('---')
print ('au revoir')


# ### Boucle for sur une énumération
# Les instructions à l'intérieur d'une boucle __for__ sont répétées pour chacune des valeurs prises par un élément d'un objet énumérable existant comme un t-uple, une liste ou un dictionnaire.

# In[3]:


# boucle for énumérant un t-uple
for i in (0, 1, 2, 3, 4, 5) : 
    print (i**2)


# In[4]:


# boucle for énumérant une liste
for i in [0, 1, 2, 3, 4, 5] : 
    print (i**2)


# In[5]:


# boucle for énumérant un dictionnaire
jours_dans_le_mois = {'janvier' : 31,
                      'février' : 28,
                      'mars' : 31,
                      'avril' : 30,
                      'mai' : 31,
                      'juin' : 30,
                      'juillet' : 31,
                      'aout' : 31,
                      'septembre' : 30,
                      'octobre' : 31,
                      'novembre' : 30,
                      'décembre' : 31}
for mois in jours_dans_le_mois :
    print ('Le mois de ' + mois + ' compte ' + f'{jours_dans_le_mois [mois]:d} jours.')
    


# ### Test d'appartenance
# On remarquera que le mot réservé __in__ réalise un test d'appartenance sur les éléments du conteneur (ou les mots-clef du dictionnaire).

# In[6]:


print (1 in (0, 1, 2, 3, 4, 5))
print (6 in [0, 1, 2, 3, 4, 5])
print ('janvier' in jours_dans_le_mois)
print (31 in jours_dans_le_mois)


# ### Boucle for sur une étendue de type range

# L'étendu de l'énumération n'est pas toujours connues au moment du codage, c'est le cas lorsque cette étendue dépend des instructions précédentes.
# 
# __range__ est un type de variable dérivée de la liste et contenant une série d'entiers 
# compris entre le premier argument $i_\mathrm{min}$ et le deuxième argument (exclu) $i_\mathrm{max}-1$ par pas de $increment$.

# In[7]:


for i in range (1, 10, 2) :
    print (i)


# Si seulement deux arguments sont donnés à __range__, ils définissent l'étendue de la série et l'incrément vaut 1 par défaut.

# In[8]:


for i in range (1, 10) :
    print (i)


# Si un seul argument est donné à __range__, $i_\mathrm{min}$ est fixé à 0 et l'incrément vaut 1.

# In[9]:


for i in range (10) :
    print (i)


# ### Boucle while
# La boucle __while__ impose la répétition d'un bloc d'instructions __tant que__ la condition d'arrêt n'est pas satisfaite.
# 
# Par exemple :
# > __Se lever__\
# __Tant que__ l'heure de partir n'est pas arrivée :\
# >>__prendre__ le petit déjeuner\
# __regarder__ l'heure
# 
# > __Partir__ à l'université
# 
# Remarques : 
# - la condition est réévaluée après chaque exécution du bloc.
# - le critère d'arrêt dépend du contexte d'exécution du programme; il est important de veiller à éviter les situations où le critère d'arrêt ne peut jamais arriver. Cette situation de boucle infinie est suceptible de saturer les ressources mémoire du système, autrement dit, le planter. C'est une des plus graves erreurs qui puissent être commises en programmation (le très fameux _stack overflow_ auquel le plus fameux forum de programmation emprunte le nom).

# ## Sélection <a class="anchor" id="selection"></a>

# Les instructions sélectionnées ne sont exécutées que si la condition prédéfinie est réalisée 
# 
# >__Si__ la condition est réalisée\
# __Alors__ exécuter l'instruction\
# __Sinon si__ une autre condition est réalisée\
# __Alors__ exécuter une autre instruction\
# ...\
# __Sinon__ exécuter l'instruction par défaut
# 
# Par exemple : 
# >__Pour__ chaque jour du lundi au dimanche :
#     >>__Si__ c'est dimanche :\
#     se lever tard\
#     prendre un brunch\
#     __Sinon si__ c'est jeudi :\
#     se lever le matin\
#     prendre le petit déjeuner\
#     reprendre du café\
#     __Sinon__ :\
#     se lever le matin\
#     prendre le petit déjeuner\

# ```python
# # syntaxe d'une instruction conditionnelle en Python
# if condition1:
#     instruction1  #le mot 'alors' ('then') est sous-entendu
# elif condition2 :
#     instruction2
# else :
#     instruction3
# ```
