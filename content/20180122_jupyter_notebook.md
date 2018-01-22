Title: Comment et pourquoi utiliser les notebook Jupyter
Date: 2018-01-22 18:16
Modified: 2018-01-22 18:16
Category: notebook
Tags: notebook, jupyter
Slug: comprendre-et-utiliser-notebook-jupyter
Authors: YesWeAreCoding
Summary: Comment et pourquoi utiliser les notebook Jupyter

# Comment et pourquoi utiliser les *notebooks* **Jupyter**

---
Tables des matières
[TOC]

---


Hello !

Vous avez peut être entendu parler des *notebook* de [Jupyter](http://jupyter.org/) et si comme moi, vous vous êtes demandé à quoi bon cela peut bien servir,
je vais vous aider à y voir un peu plus clair.  
Déjà, à quoi ils ressemblent ? Vous pouvez trouver une large [gallerie d'exemple ici](http://nb.bianp.net/sort/views/).  
Voyons un peu ce que on peut en faire.

## Cas d'utilisation
Les *notebook* ressemblent finalement à des pages Web dynamique, avec des champs que l'on peut exécuter et voir le résultat en direct. Les grands cas d'utilisation sont souvent en sciences
car c'est très pratique pour présenter des résultats pas à pas, expliquer des contextes. On les retrouvent souvent dans les domaines de :
* machine learning
* mathématiques
* physiques
* chimie, biologie
* géographie (avec affichage de cartes)
* analyse de signal
* *etc*

Pour ma part, je m'en sert généralement pour tester des bouts de code (genre un copier/coller de *stackoverflow*) ou pour présenter du code à des collègues, ou encore lorsque
je m'entraine au *machine learning*. Bref, c'est utile dans les cas où l'on a besoin de pédagogie ou faire des tests en *scratch* (= à l'arrache).

Convaincu ? Pas encore ? Vous pouvez le tester en *live* sur [try.jupyter.org](https://try.jupyter.org/).

## Installation

Je détaille ici une installation sous Mac/Linux, pour Windows, c'est à l'aide d'Anaconda mais le principe reste le même.  
Créez tout d'abord un environnement virtuel :  
`python -m venv notebooks`  
Puis activez le : `source venv/bin/activate`  
Une fois fait : `pip install jupyter`  
Ce n'était pas bien compliqué ^^. N'oubliez d'ajouter les libraires dont vous avez besoin lorsque vous faites votre `pip install`.

## Démarrage

Depuis le terminal, après avoir activer l'environnement virtuel, vous n'avez plus qu'à exécuter `jupyter notebook`. Cette commande va lancer un navigateur Web
(ou ouvir un nouvel onglet) où vous pourrez voir un petit navigateur de fichier (par défaut [localhost:8888](http://localhost:8888]). On va pouvoir maintenant créer un nouvel notebook 
en utilisant le menu en haut à droite `New -> Python 3`. Vous lancez ainsi un nouveau **kernel** de type *Python 3*. Si le précise, c'est que l'on peut en fait coder avec beaucoup d'autres langages
via ces *kernels*. Vous trouverez ici la [liste de ces noyaux](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

## Utilisation

A partir de là, c'est assez simple. Vous cliquez sur une cellule vide, vous tapez votre code puis vous cliquez sur le bouton **Run**. Il y a
quelques raccourcis clavier qui permettent de se simplifier la vie, je vous fait un petit *cheat sheet* pour tout avoir sous la main :  

| Raccourci | Action | Exemple
| - | - | - |
| `shift` + `enter` | exécute le contenu d'une cellule puis<br>crée une nouvelle cellule vide au dessous | |
| `alt` + `enter` | exécute le contenu d'une cellule<br>sans en créer de nouvelle | | 
| `!` | exécute une commande shell | `!pip install numpy` |
| `%%time` | mesure le temps d'exécution | `CPU times: user 1.23 ms, sys: 4.82 ms, total: 6.05 ms` |


Tous les raccourcis peuvent se retrouver dans le répertoire **Help > Keyboard Shortcuts**.  
A noter également que toutes les [`magic` commandes d'IPython](http://ipython.readthedocs.io/en/stable/interactive/magics.html) sont supportées.
