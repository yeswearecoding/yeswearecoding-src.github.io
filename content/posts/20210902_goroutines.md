---
title: "[Golang] Programmation concurrente avec des goroutines"
categories: [golang]
tags: [concurrence, multithreading]
date: 2021-09-02T09:31:35+02:00
draft: false
---

Nouvelle année, nouveau challenge ! Ca fait pas mal de temps de je lorgne sur le Go (ou Golang) et ça y est, il est venu le temps de s'y mettre !
Avant cela, j'ai (un peu) mis à jour mon site et rajouter un lien pour ma page LinkedIn : n'hésitez pas à me suivre ou m'ajouter afin de recevoir les prochaines mises à jour 😊.

Le Go (ou Golang) est un langage développé depuis quelques années désormais (plus de 10 ans) par une équipe de Google, et pas des débutants ! Notamment [Brian Kernighan](https://fr.wikipedia.org/wiki/Brian_Kernighan), éminent informaticien en C et autre. Ils ont alors développé ce langage pour simplifier l'utilisation du multithreading, principe au coeur du Go.

Je vais vous présenter içi les `goroutines`, principe de base pour la mise en oeuvre du multithreading en Go.

## Définitions

Programmation concurente : composition de plusieurs activités autonomes.

Go supporte deux types de programmation concurrente : 

* CSP (*communicating sequential processes* - processus séquentiels de communication). Les variables sont passées entre des activités indépendamment mais les variables sont la plus part du temps confinées à une seule de ces activités.
* *shared memory multithreading* (multithreading à mémoire partagée)

goroutine : activité exécutée en concurrence (on peut aussi dire en paralèlle)