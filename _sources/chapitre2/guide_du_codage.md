# Guide du codage

Ce chapitre a pour but de fournir des méthodes pratiques pour améliorer les compétences de 
programmation en facilitant la recherche d'erreurs.

L'idée directrice de cette démarche de programmation est de **décomposer le programme en plusieurs niveaux de sous-programmes**, jusqu'à la mise en oeuvre d'opérations élémentaires.
Les sous-décompositions contribuent à la lecture du programme principal et elles sont plus simple à programmer et à débugguer.
En contrepartie, un effort de structuration est nécessaire pour que les différents éléments du programmes puissent se transmettre les données nécessaires pour fonctionner ensemble.

La plupart des languages de programmation incluent les outils dédiés à cette structuration du code :
- Les **fonctions**  rassemblent certaines séquences d'instructions afin de rendre le code plus lisible et plus modulable.

- Les **modules** rassemblent plusieurs fonctions suivant leur champ d'application. 

- Les **classes** constituent une structure de données à part entière du fait qu'elles rassemblent des variables (comme un conteneur) et des fonctions (comme un module). Leur intérêt vient de ce qu'une _instance de classe_ (_i.e._ un *objet* du type de la classe  rassemblant ses variables propres) simplifie la transmission de l'ensemble des données pertinentes pour l'objet d'une fonction à l'autre.


```{tableofcontents}
```
