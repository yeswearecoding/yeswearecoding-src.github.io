---
title: "Comprendre les décorateurs"
categories: [python]
date: 2018-02-06T12:23:00+01:00
comments: true
draft: false
---

Hello !

Vous avez peut-être déjà rencontré lors de la consultation de code écrit par quelqu'un d'autre la présence d'un `@` suivi d'un nom juste avant la définition d'une fonction et vous vous êtes posé la question "à quoi cela peut-il bien servir ?".

Voyons cela ensemble.

## Poser les bases

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

## Appliquer

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

## Pour aller plus loin

Je vous laisse admirer un magnifique décorateur issu du code de [Bottle](https://bottlepy.org) qui est un micro-framework Web qui tient en un seul fichier (j'adore) :

```python
def route(self,
            path=None,
            method='GET',
            callback=None,
            name=None,
            apply=None,
            skip=None, **config):
    """ A decorator to bind a function to a request URL. Example::
            @app.route('/hello/<name>')
            def hello(name):
                return 'Hello %s' % name
        The ``<name>`` part is a wildcard. See :class:`Router` for syntax
        details.
        :param path: Request path or a list of paths to listen to. If no
            path is specified, it is automatically generated from the
            signature of the function.
        :param method: HTTP method (`GET`, `POST`, `PUT`, ...) or a list of
            methods to listen to. (default: `GET`)
        :param callback: An optional shortcut to avoid the decorator
            syntax. ``route(..., callback=func)`` equals ``route(...)(func)``
        :param name: The name for this route. (default: None)
        :param apply: A decorator or plugin or a list of plugins. These are
            applied to the route callback in addition to installed plugins.
        :param skip: A list of plugins, plugin classes or names. Matching
            plugins are not installed to this route. ``True`` skips all.
        Any additional keyword arguments are stored as route-specific
        configuration and passed to plugins (see :meth:`Plugin.apply`).
    """
    if callable(path): path, callback = None, path
    plugins = makelist(apply)
    skiplist = makelist(skip)

    def decorator(callback):
        if isinstance(callback, basestring): callback = load(callback)
        for rule in makelist(path) or yieldroutes(callback):
            for verb in makelist(method):
                verb = verb.upper()
                route = Route(self, rule, verb, callback,
                                name=name,
                                plugins=plugins,
                                skiplist=skiplist, **config)
                self.add_route(route)
        return callback

    return decorator(callback) if callback else decorator
```

Les incontournables Sam et Max :

[Comprendre les décorateurs Python pas à pas (partie 1)](http://sametmax.com/comprendre-les-decorateurs-python-pas-a-pas-partie-1/)  
[Comprendre les décorateurs Python pas à pas (partie 2)](http://sametmax.com/comprendre-les-decorateur-python-pas-a-pas-partie-2/)

Un article (en anglais) qui donne plus de détails et les bonnes pratiques :  
[The decorators they won't tell you about](https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb)

Bon code !
