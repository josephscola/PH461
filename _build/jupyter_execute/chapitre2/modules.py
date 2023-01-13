#!/usr/bin/env python
# coding: utf-8

# ## Modules

# Les modules sont également désignés par le terme de __bibliothèques__ (_library_ en anglais) qui illustre parfaitement l'usage qui en est fait : on consulte la documentation des fonctions disponibles et on emprunte les fonctions nécessaires.
# La force du langage Python réside dans l'ouverture de ses bibliothèques : une multitude de contributeurs·rices met à disposition de toutes et tous les modules qu'ils ou elles développent. 
# La communauté Python est très active et la plupart des bibliothèques bénéficient d'une maintenance régulière qui garantie la fiabilité.
# En conséquence, si une fonction a déjà été écrite, il est très fortement déconseillé de la réécrire (puisque dans le meilleur des cas, elle ne serait qu'aussi bien).

# Pour qu'une fonction puisse être appelée par un programme, il faut que l'interpréteur y ait accès, c'est-à-dire :
# - que le fichier contenant le script de la fonction soit stocké localement (installation du module)
# - que le module contenant la fonction soit inclus dans les instructions à interpréter (importation du module)

# #### Création du module PH461

# 1. Créer un fichier texte vierge intitulé PH461.py dans le répertoire PH461/TD1 (celui du notebook du TD1)
# 2. Copier les fonctions du TD dans le fichier PH461.py
# 3. Importer les fonctions du modules dans un script ou ue cellule de notebook par la commande __import__ :

# In[1]:


import PH461


# L'appel d'une fonction issue d'un module doit mentionner le nom du module :

# In[ ]:


PH461.printcoucou ()


# Il est parfois commode de donner un alias au nom du module :

# In[ ]:


import PH461 as ph
ph.printcoucou ()


# L'importation d'un module enregistré ailleurs que dans le répertoire de travail sera vue en TP.