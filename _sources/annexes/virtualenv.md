

# Utiliser ne environnement virtuel

Développer un projet dans un _environnement virtuel_ n'est pas indispensable à court terme mais le devient avec le temps afin de garantir 
- la maintenance
- l'extension
- le partage 
- la stabilité globale de l'installation Python

Un environnement virtuel est en réalité une distribution Python complète et indépendante de la distribution installée sur l'ordinateur. Cela permet de dédiée une distribution et ses dépendances à un seul projet. En pratique, les modules nécessaires importés au projet sont installés dans l'environnement virtuel uniquement.
- les modules python évoluent certaines mises à jour requiert une modification (mineure) des projets qui les appellent. Les environnement virtuels permettent de faire coexister sur une machine plusieurs versions d'un même module de sorte qu'il n'est pas indispensable de vérifier quelles sont les modifications à introduire sur tous les projets à chaque mise à jour de modules.
- facilite le partage d'un code puisqu'il suffit de joindre au projet la liste des modules qu'il importe pour transmettre pour que le projet puisse fonctionner sur une autre machine (à commencer par la vôtre si vous changez d'ordinateur).

Plus d'information sont accessibiles ![ici](https://www.dabapps.com/insights/introduction-to-pip-and-virtualenv-python/)

La procédure d'installation suivante est orientée Linux. Elle utilise l'outil d'instalation _pip_. 
Des informations sur l'installation de _pip_ sous windows sont accessibles [ici](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows=)


## Installation
```bash
pip install virtualenv
```

## Comment créer un environnement virtuel ?
Avec python3.10
```bash
cd ~/mon_projet/
virtualenv -p python3.10 env
```

Avec python3.9 et les versions inférieures
```bash
cd ~/mon_projet/
virtualenv env
```
L'environnement est alors localisé the environment localisé dans le répertoire  ~/mon_projet/env/

## Travailler l'environnement virtuel
Une fois installé, l'environnement virtuel doit être activé par la commande
```{bash}
source env/bin/activate
```

la chaine de caractères _(env)_ s'ajoute à l'amorce de commande pour signaler que le terinal travaille dans l'environnement _env_.

Les modules peuvent être installés un par un dans l'environnement virtuel 
```bash
pip install package-name
```

Mais il est recommandé de rassembler la liste des modules dans un fichier _requirements.txt_ en précisant éventuellement la version souhaitée 

```bash
requirement text file :
module1
module2
module3>=1.0,<=2.0
```

puis de les installer en une seule commande 
```bash
python3 -m pip install -r requirements.txt
```

## Utiliser un notebook dans un environnement virtuel 

La procédure de création et d'activation virtuelle est la même que précédemment
```bash
cd ~/mon_projet/
virtualenv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

```{warning}
Il est fréquent que plusieurs versions de python (par exemple 3.8, 3.9 et 3.10) coexistent sur une machine. Dans ce cas, il faut s'assurer que l'environnement virtuel utilise la même version que le notebook.
```

A quoi s'ajoute l'ajout du noyau Python de l'environnement virtuel _env_ à la liste de ceux accessible depuis le notebook
```bash
ipython kernel install --user --name=env
```

Ensuite, l'environnement virtuel _env_ peut être choisi dans le notebook parmi les noyaux Python du menu Kernel > Change kernel > env

La désinstallation du noyau (à la fin du projet) est effectuée par la commande 
```bash
jupyter-kernelspec uninstall env
```
