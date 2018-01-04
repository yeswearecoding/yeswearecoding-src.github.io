Title: Cheatsheet de challenge
Date: 2017-12-16 13:37
Modified: 2017-12-16 13:37
Category: challenge
Tags: challenge, optimisation
Slug: challenge-cheatsheet
Authors: YesWeAreCoding
Summary: Liste de tricks appris lors de challenge

Hello,

A force de faire quelques challenge sur [HackerRank](https://www.hackerrank.com/yeswearecoding), j'ai
noté quelques *tricks* que j'oublie souvent. Du coup, je met ça içi. Servez-vous :-)


## *list* et *set*

### intersection de deux listes
Récupérer l'intersection entre deux listes (en fait, uniquement si l'une des deux peut être transformée en set):

    :::python
    a = ['un', 'deux', 'trois']
    b = ['dites', 'trente', 'trois']
    inter = list(filter(set(a).__contains__, b))


Résultat :

    :::python
    print(inter)
    ['trois']


## module *itertools*

### toutes les combinaisons d'une liste de listes
Imaginons que j'ai une méga liste qui contient des listes:  

    :::python
    mega_liste = [['a', 'b'], ['c', 'd', 'e'], ['f']]

Tout le job de génération des combinaison se fait par la fonction *product* de *itertools*. La doc (en français !) se trouve ici : [doc itertools](https://docs.python.org/fr/3.6/library/itertools.html#itertools.product). Les explications restent un peu pas forcément hyper claires mais j'espère que ce petit exemple vous permettra d'en comprendre l'utilité.  

    :::python
    import itertools
    combinaisons = itertools.product(*mega_liste)

On utilise ici l'opérateur *splat* (l'étoile) pour faire de l'*unpacking* sur 'mega_liste'. Un (excellent) article sur ça : [SametMax - operateur splat ou étoile en Python](http://sametmax.com/operateur-splat-ou-etoile-en-python/).  
On obtient alors :  

    :::python
    for combinaison in combinaisons:
        print(combinaison)
    
    ('a', 'c', 'f')
    ('a', 'd', 'f')
    ('a', 'e', 'f')
    ('b', 'c', 'f')
    ('b', 'd', 'f')
    ('b', 'e', 'f')