#!/usr/bin/env python
# coding: utf-8

# ## Préambule : Présentation de l'environnement de programmation en Python <a class="anchor" id="chapter1"></a>
# 
# * [Quel équipement pour le PH641 ?](#equipement)
# * [Installation de l'interpréteur Python3](#installation_py)
# * [Exécuter des commandes Python](#run_py)
# * [Installation de l'environnement de travail Jupyter-notebook](#isntallation_nb)

# ### Quel équipement pour le PH641 ? <a class="anchor" id="equipement"></a>
# 
# Tous les exercices étant sur machine, il est obligatoire de venir en cours muni d'un ordinateur, le vôtre ou un cartable numérique.
# L'interpréteur Python peut-être installé sur les systèmes d'exploitation Linux, Windows et MacOS.
# Le département de mathématique de l'UVSQ met à disposition un interpréteur en ligne accessible avec les identifiants UVSQ : 
# [jupyter.ens.uvsq.fr](https://jupyter.ens.uvsq.fr/)
# Pour ce cours, il n'est donc pas indispensable d'installer Python sur son propre équipement, mais c'est fortement recommandé pour le confort de travail.

# ### Installations de l'interpréteur Python3 <a class="anchor" id="installation_py"></a>
# 
# L'interpréteur est le programme qui lit et exécute les commandes Python. 
# Il s'installe comme un programme ordinaire.
# 
# #### Sous windows :
# distribution Anaconda + Python3.7
# 
# #### Sous Linux : 
# installé par défaut dans la plupart des distribution (Ubuntu, Raspberry pi)
# 
# #### Sous MacOS :
# voir la [documentation en ligne](https://docs.anaconda.com/anaconda/install/mac-os/)

# ### Exécuter des commandes Python <a class="anchor" id="run_py"></a>
# #### Commandes individuelles
# Ouvrir un terminal et exécuter la commande 
# <pre><code> python3 </code></pre>
# 
# Le terminal propose alors de saisir des commandes pouvant être exécutées directement.
# 
# #### Exécuter un script
# Un script estun fichier contenant une séries d'instructions qui seront exécutées para un interpréteur comme Python.
# Les commandes d'un _script_ sont exécutées séquentiellement par un _interpréteur_ à la différence d'un _programme_ qui est dans un premier temps converti dans un premier temps en _exécutable_ par un _compilateur_ puis exécuté par le processeur.
# A tache identique, le temps d'exécution d'un  _programme compilé_ est deux à trois ordres de grandeurs plus court que celui d'un _script interprété_;
# En pratique, on se détournera de Python, souvent au profit du langage C, pour des applications embarquées ou nécessitant d'importantes ressources de processeur.
# 
# Les scripts Python sont de simples fichiers textes contenant la séquence des commandes; pour être reconnus par l'interpréteur, ces fichiers doivent impérativement porter l'extension .py.
# Un script Python peut être exécuté depuis le terminal par la commande :
# <pre><code> python3 premier_script_Python.py </code></pre>

# ### Environnement de travail Jupyter-notebook <a class="anchor" id="installation_nb"></a>
# 
# Dans ce cours, les scripts ne seront pas exécutés dans le terminal mais dans un _jupyter notebook_.
# Cet éditeur offre un environnement de développement convivial est particulièrement adapté à la rédaction scientifique (compte-rendu de TP, rapport d'analyse, article scientifique, ...).
# Ce support de cours est un _jupyter notebook_.
# 
# #### Installation sous Linux :
# - Installer notebook : 
# <pre><code> pip install notebook </code></pre>
# 
# - Installer l'extension nbextensions de notebook:
# <pre><code> jupyter contrib nbextension install --user </code></pre>
# 
# - Activer l'éditeur convivial des extensions de notebook :
# <pre><code> jupyter nbextensions_configurator enable </code></pre>
# 
# - Lancer un notebook de jupyter :
# <pre><code> jupyter notebook </code></pre>

# ### Arborescence de votre répertoire de travail <a class="anchor" id="commandes_jupyter"></a>
# Il est nécessaire de donner à l'arborescence du répertoire de travail une structure simple et lisible qui devra être employée pour chaque projet.
# En premier lieu, créez un répertoire __PH461__ à l'intérieur duquel vous créerez :
# - __1 répertoire projet__ contenant le _jupyter  notebook_ du projet
#     - __1 sous-répertoire module__ pour les fonctions spécifiques, structuré comme un module
#     - __1 sous-répertoire data__ pour les données d'entrée
#     - __1 sous-répertoire output__ pour les données de sortie
# - __1 répertoire routines__ dédié aux fonctions appelées par plusieurs projets

# ### Premier contact avec le serpent 
# #### Exécution d'une instruction avec notebook

# In[1]:


print ('Pour afficher cette chaîne de caractères, vous avez cliqué sur le bouton "Exécuter"')


# In[2]:


print ('Pour afficher cette chaîne de caractères, vous avez pressé "Ctrl-Enter"')
print ('La cellule active n\'a pas changé')


# In[3]:


print ('Pour afficher cette chaîne de caractères, vous avez pressé "Shift-Enter"')
print ('C\'est la cellule suivante qui est maintenant active')


# In[4]:


print ('Pour afficher cette chaîne de caractères, vous avez pressé "Alt-Enter"')
print ('Une nouvelle cellule a été créée après celle-ci')


# #### Commentaires
# Le caractère # marque le début d'un commentaire jusqu'à la fin de la ligne.

# In[5]:


print ('Cette ligne est commentée') # commentaire de la ligne
#print ('Il a fallu retirer le caractère # pour que cette chaîne soit affichée') 

