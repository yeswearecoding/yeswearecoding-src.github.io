Title: Comprendre les décorateurs
Date: 2018-02-06 12:23
Modified: 2018-02-06 12:23
Category: design patterns
Tags: python, design patterns, decorator
Slug: comprendre-decorateur
Authors: YesWeAreCoding
Summary: Utiliser les décorateurs efficacement

Hello !

Vous avez peut-être déjà rencontré lors de la consultation de code écrit par quelqu'un d'autre la présence d'un `@` suivi d'un nom juste avant la définition d'une fonction et vous vous êtes posé la question "à quoi cela peut-il bien servir ?".

Voyons cela ensemble.

---
Sommaire

[TOC]

---

# Poser les bases

En Python, les fonctions sont des [Objet de première classe](https://fr.wikipedia.org/wiki/Objet_de_premi%C3%A8re_classe), c'est à dire qu'elles se comporte comme n'importe quel objet.

Exemple :

```python

# une fonction de toute beauté
def ma_fonction():
    print('hello toto')
```

Comme elle se comporte comme un objet, je peux la stocker dans une variable puis l’appeler en ajoutant les parenthèses lors de l'appel de ma variable :

```python
tata = ma_fonction
```

vérifions son type :
```python
print(type(tata))

<class 'function'>
```

je peux donc l’appeler : (notez bien l'ajout des parenthèses)

```python
tata()

hello toto
```

Magnifique. Génial. Bon, et on fait quoi maintenant que l'on sait ça ?

# Appliquer

Les décorateurs sont souvent définis par des fonctions qui prennent des fonctions en arguments et qui retournent des fonctions. C'est pas clair ? C'est normal :-). Voyons un exemple simple. Il faut juste se dire qu'un décorateur est quelque chose qui vient entourer une fonction (la décorer, telle l'artiste qui décore un vase pour vous donner une image).

Codons un décorateur qui a pour fonction de faire un *timer* pour savoir combien de temps la fonction décorée met à s'exécuter.

```python
import time

def timer(une_fonction):
    def osef(parametres):
        debut = time.time()
        res = une_fonction(parametres)
        print("On a mis {:.1f} secondes".format(time.time()-debut))
        return res
    return osef
```

Définissons une fonction pour laquelle on souhaite connaitre son temps d'exécution :

```python
@timer
def attendons(secondes):
    for el in range(secondes):
        time.sleep(1)
```

Puis vérifions notre résultat :

```python
attendons(2)

On a mis 2.0 secondes
```

N'est-ce pas magnifique ? C'est merveilleux Jean-Pierre.

Plus sérieusement, nous avons vu comment on construit un décorateur assez simple et comment il s'utilise. Maintenant que vous avez vu le principe, vous pourrez développer les vôtres facilement !

Petite mise en garde : c'est comme tout, les décorateurs s'utilisent uniquement **quand c'est utile !!** Inutile d'étaler votre nouvelle connaissance juste pour le plaisir de coder :-) (bon, si un peu quand même histoire de s’entraîner).

# Pour aller plus loin

Je vous laisse admirer un magnifique décorateur issu du code de [Bottle](https://bottlepy.org) qui est un micro-framework Web qui tient en un seul fichier (j'adore) :

[gist:id=4f62c0be5c1134e265b8dcc1b904268b]

Les incontournables Sam et Max :

[Comprendre les décorateurs Python pas à pas (partie 1)](http://sametmax.com/comprendre-les-decorateurs-python-pas-a-pas-partie-1/)  
[Comprendre les décorateurs Python pas à pas (partie 2)](http://sametmax.com/comprendre-les-decorateur-python-pas-a-pas-partie-2/)

