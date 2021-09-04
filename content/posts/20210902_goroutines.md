---
title: "Programmation concurrente avec des goroutines"
categories: [golang]
tags: [concurrence, multithreading]
date: 2021-09-02T09:31:35+02:00
draft: false
showToc: true
TocOpen: false
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

goroutine : activité exécutée en concurrence

## Exemples

Maintenant que nous avons vu le principe de base, place aux exemples !

### Basique

On va faire un simple `hello world !` mais en utilisant une `goroutine`. On va écrire une fonction `say` qui prend une `string` en argument et que l'on appelera en tant que `goroutine` (avec le mot-clé `go`) et qui nous affichera "hello". Voyons ce que ça donne :

```go
package main
import "fmt"
	

func say(s string) {
	fmt.Println(s)
}

func main() {
    go say("hello")
	fmt.Println("world !")
}
```

La sortie :

```bash
world !
```

Quoi ?!? Mais il manque un bout !!! 😱😱😱  
Explication : la boucle principale `main` n'attend pas la fin de l'exécution de la `goroutine`. Pour le moment, on va résoudre ça avec un simple `sleep`. On modifie le code ainsi :

```go
package main

import (
	"fmt"
	"time"
)

func say(s string) {
	fmt.Println(s)
}

func main() {
	go say("hello")
	fmt.Println("world !")
	time.Sleep(500 * time.Millisecond)
}
```

On obtient en sortie :

```bash
world !
hello
```

Ah !!!!! Voilà ! On obtient bien ce que l'on souhaite en sortie mais c'est loin d'être optimal...

On peut faire beaucoup mieux !! Place à la suite 😉

### Attendre plusieurs goroutines

Lorsque l'on a besoin d'attendre que une ou plusieurs `goroutine` finissent, on utilise le packet `sync` et la fonction [sync.WaitGroup](https://pkg.go.dev/sync#WaitGroup). Elle est utilisé pour bloquer le `main` (ou toute autre fonction appelante) jusqu'à ce que toutes les `goroutine` aient terminé leur travail. Un exemple parlant (adapté de l'article [How to wait for all goroutines to finish in Golang](https://goinbigdata.com/golang-wait-for-all-goroutines-to-finish/)) :

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(wg *sync.WaitGroup, id int) {
	defer wg.Done() //décrémentation (lorsque la goroutine a terminé)

	fmt.Printf("Worker %v: Début\n", id)
	time.Sleep(time.Second)
	fmt.Printf("Worker %v: Terminé\n", id)
}

func main() {
	var wg sync.WaitGroup // déclaration

	for i := 0; i < 5; i++ {
		fmt.Println("Main: Lancement du Worker", i)
		wg.Add(1) // incrémentation d'une unité
		go worker(&wg, i) // passage par adresse
	}

	fmt.Println("Main: En attente des Workers")
	wg.Wait()
	fmt.Println("Main: Terminé")
}
```

Ce qui donne :

```bash
Main: Lancement du Worker 0
Main: Lancement du Worker 1
Main: Lancement du Worker 2
Main: Lancement du Worker 3
Main: Lancement du Worker 4
Worker 0: Début
Worker 4: Début
Worker 2: Début
Main: En attente des Workers
Worker 1: Début
Worker 3: Début
Worker 1: Terminé
Worker 0: Terminé
Worker 4: Terminé
Worker 2: Terminé
Worker 3: Terminé
Main: Terminé
```

N'est-ce pas formidable ?

L'utilisation de `WaitGroup` est assez simple :

* déclation dans le `main`
* incrémentation avec `.Add(1)` avant l'appel de la `goroutine`
* appel de la `goroutine` avec passage par adresse du `WaitGroup`
* décrémentation du `WaitGroup` au sein de la goroutine avec `.Done()`
* en fin de bloc, on attend la fin des `goroutine` avec `.Wait()`
  
Notez l'utilisation de `defer` pour la décrémentation dès le début de la `goroutine`. Ce mot-clé permet de s'assurer que la fonction qui le suit sera bien appelée à la fin du bloc. On le retrouve pour la lecture des fichiers : on s'assure ainsi que ce dernier sera bien fermé à la fin du traitement.

### goroutine anonyme

Lorsque la `goroutine` ne fait quelques lignes (pas trop, sinon le code devient vite illisible...), il est possible d'utiliser une fonction anonyme. Voyons avec l'exemple précédent ce que cela change :

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup // déclaration

	for i := 0; i < 5; i++ {
		fmt.Println("Main: Lancement du Worker", i)
		wg.Add(1) // incrémentation d'une unité
		
		go func(id int) { // fonction anonyme
			defer wg.Done() //décrémentation (lorsque la goroutine a terminé)

			fmt.Printf("Worker %v: Début\n", id)
			time.Sleep(time.Second)
			fmt.Printf("Worker %v: Terminé\n", id)
		}(i)
	}

	fmt.Println("Main: En attente des Workers")
	wg.Wait()
	fmt.Println("Main: Terminé")
}
```

C'est un peu plus concis 😊

## Conclusion

Voilà, c'est terminé pour cette petite présentation ! J'ai utilisé également les livres suivant dans mon apprentissage :

* [The Go Programming Language](https://amzn.to/3gWR6By)
* [Le langage Go](Go Programming Language, The)

A bientôt !
