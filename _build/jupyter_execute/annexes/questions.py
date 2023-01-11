#!/usr/bin/env python
# coding: utf-8

# #### Dysfonctionnement de __ordre_de_l_erreur__ lorsque le plus petit chiffre significatif est 0
# Il a été relevé par Mme Pop durant la séance que la fonction __ordre_de_l_erreur__ surestimait l'ordre de l'erreur $\varepsilon$ du plus petit chiffre significatif lorsque celui-ci vaut 0.
# Effectivement, la fonction détermine son résultat $n$ par le critère :
# $$ \left\{ \mathrm{min}\, n,\, n  \in\mathbb{N}^+\right\},\quad \varepsilon \cdot 10^{n} \le \mathrm{floor} (\varepsilon \cdot 10^{n}) $$
# $n$ étant défini comme le plus petit nombre de décalage à droite de la virgule nécessaire pour que toutes les décimales non nulles se retrouvent à gauche de la virgule.
# Or ce critère n'est pas manifestement plus valide lorsque qu'un des chiffres significatifs de l'erreur est nul (_e.g._ $\varepsilon = 0.50$).
# 
# Mon erreur vient du fait que la question ne se pose pas lorsque l'incertitude est connue avec 1 seul chiffre significatif comme c'était le cas dans les exercices de L1 d'où j'ai repris l'algorithme;
# ce chiffre significatif unique n'est jamais nul par la force des choses (et par celle de l'arrondi à la décimale supérieure).
# Lorsque l'incertitude s'exprime avec plusieurs chiffres significatifs, la présence d'un zéro à droite n'a pas une signification unique :
# - soit il signifie l'ajout d'un terme $0\cdot 10^{-n},\, n\in \mathbb{N}^+$,
# - soit il informe sur l'ordre de grandeur de la précision avec laquelle l'incertitude est connue.
# 
# En conséquence, la valeur numérique de l'incertitude ne suffit pas pour que le programme connaisse l'ordre de l'erreur sans ambibuïté.
# Il est donc nécessaire de lui fournir une information supplémentaire comme le nombre de chiffres significatifs de l'incertitude.
# Ce dysfonctionnement du programme provient donc d'une erreur de définition du problème, tout en amont du processus de programmation : l'algorithme n'est opérationnel que pour une erreur connue avec 1 chiffre significatif et il ne peut pas être étendu simplement à d'autres cas de figure. Ces cas de figures doivent être traités comme des _exceptions_ dans ce programme.
# 
# Bien vu Mme Pop.

# #### Comment afficher directement un tableau formatté sans devoir copier-coller le résultat de la cellule ?

# In[1]:


from IPython.display import display, Markdown

tableau = '| | |\n|:-:|:-:|\n| 1 | 2 |\n| 2 | 4 |'
display (Markdown (tableau))


# ---

# #### Pourquoi if 12 est-elle une instruction valide ?

# In[2]:


a = 1
print (a == True)
if a:
	print ('a satisfait la condition')
print ('la valeur de a.__bool__() est ', a.__bool__ ())

b = 12.
print (b == True)
if b:
	print ('b satisfait la condition')

print ('la valeur de b.__bool__() est ', b.__bool__ ())


# #### réponse : 
# requête duckduckgo : "python if statement non boolean" \
# https://stackoverflow.com/questions/38237668/if-statement-with-no-logical-operators-in-python
