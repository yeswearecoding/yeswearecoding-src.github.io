---
title: "Golang : programmation concurrente avec des goroutines"
date: 2021-09-02T09:49:53+02:00
comments: true
draft: false
---




# Les canaux (channels) en Go



L'appel à une *goroutine* se fait en utilisant le mot-clé *go* devant la fonction :
```go
f() // appel de la fonction f, attent son retour avant de continuer (on dit bloquant)
go f() // créé une nouvelle goroutine qui appelle f() mais n'attend pas le retour (non bloquant)
```

