---
title: "A la découverte de MicroPython sur ESP32"
categories: [embarqué]
tags: [micropython]
date: 2018-08-24T07:51:00+01:00
comments: true
draft: false
---

Hello ! Comme c'est les vacances et qu'il faut bien s'occuper (#geeker) un peu, j'ai joué un peu avec [MicroPython](http://micropython.org/) sur un microcontrôleur de type ESP32. Je me suis basé sur la lecture de [Programmer en MicroPython](https://amzn.to/2PBEEIv), qui est le seul livre en français sur le sujet. Bon, il y en 2-3 de plus en anglais, mais rien de folichon non plus...  
Pour le matériel, j'ai utilisé ma carte [ESP32 Gateway de chez Olimex](https://amzn.to/2PAWV8O) que j'avais sous la main.  
Voyons voir ce que l'on peut faire avec tout ça! 🕵️‍♂️

## Présentation de MicroPython

Il s'agit d'un projet lancé en 2013 sur Kickstarter pour financer le portage d'une version légère de Python sur des microcontrôleurs. Enthousiasme de la communauté, les objectifs de la campagne sont largement dépassées et le projet est finalisé. Il est associé à un matériel spécifiquement développé pour ce système, la [PyBoard](https://amzn.to/2BFE0Xu), qui comporte plein d'entrées/sorties (des GPIO, comme sur les Raspberry) et qui est pleinement supportée par le projet.  
Plusieurs autres cartes sont supportées : [WiPy de chez Pycom](https://amzn.to/2PDvGue), les ESP8266, les ESP32, des cartes à base de STM32 comme la NUCLEO-F401RE, la [NUCLEO-F767ZI](https://amzn.to/2N9kfsq), la [NUCLEO-L476RG](https://amzn.to/2MPhOhN) ou bien encore la [Espruino Pico](https://amzn.to/2o6SE0d). Bref, il y a du choix ma petite dame !  
Et maintenant, c'est le moment de se retrousser les manches et de mettre les mains dans le camboui !  
💪

## Installation du firmware

## Prérequis

### Drivers USB/série

Les cartes microcontrôleur utilisent très généralement des convertisseur USB-série afin de les utiliser facilement depuis son PC. Mais cela nécessite l'installation des drivers associés.  
Pour ma carte, c'est le CH340. Je suis sous Mac, j'ai utilisé la méthode d'installation *via* Homebrew trouvée ici : [CH340G CH34G CH34X Mac OS X driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver). Une fois branchée votre carte, récupérer le nom du point de montage (par exemple avec un `sudo dmesg | grep dev`). Pour moi, c'est `/dev/cu.wchusbserial1410` que j'utiliserai pour la suite de cet article, n'oubliez pas d'adapter à votre cas (généralement `/dev/ttyUSB0` pour Linux, `COMx` (où x est un nombre) pour Windows).  

### Screen

Autre élément, on aura besoin d'utiliser un shell à travers une liaison série. Sous Linux ou Mac, assurez-vous d'avoir `screen` d'installé. Petit rappel / guide de survie des commandes de cet outil :  
`Ctrl A` puis `Ctrl D` pour détacher une session. Vous allez sortir de `screen` mais votre session sera toujours active. Vous pourrez la retrouver avec `screen -r`.  
Pour fermer une session : `Ctrl A` puis `:` puis `quit` (tapez entrée pour valider).

## Créer un environnement virtuel

Nous allons avoir besoin de plusieurs librairies en Python. Pour une meilleure organisation, je vous conseille (comme tout projet d'ailleur) de créer un environnement virtuel dédié.  
J'utilise [Pipenv](https://pipenv.readthedocs.io/en/latest/) pour faire ça facilement et rapidement :

```bash
mkdir micropython-esp32
cd micropython-esp32
pipenv install esptool adafruit-ampy
pipenv shell
```

`esptool` permet d'effacer puis flasher un microcontrôleur, `adafruit-ampy` sert à lister les fichiers présents, en récupérer (`get`) ou en déposer (`put`).

Nous somme désormais dans notre environnement virtuel avec les librairies qui vont bien. On peut passer à la suite.

## Flasher sa carte

Bon, les exemples que je donne sont valables (testés) avec ma carte mais devrait fonctionner (à quelques adaptations mineures près) avec les autre carte.  
Pour la suite, on va récupérer le firmware, effacer la mémoire du microcontrôleur puis la réécrire avec le MicroPython.

### Récupérer le dernier firmware

Tout se trouve sur la page [Downloads](http://micropython.org/download). Récupérez la version qui correspond à votre matériel. Pour la ESP32 Gateway de chez Olimex, c'est dans **Firmware for ESP32 boards** puis **Standard firmware**. Un coup de `wget`:

```bash
wget http://micropython.org/resources/firmware/esp32-20180824-v1.9.4-479-g828f771e3.bin
```

### Effacer la mémoire du microcontrôleur

On utilise la librairie `esptool` pour effacer la mémoire de l'ESP32 :

```bash
esptool.py --chip esp32 erase_flash
```

Il devrait trouver automatique le point de montage. Si ce n'était pas le cas, vous pouvez le spécifier avec l'option `--port`.  
Si vous avez des soucis, vous pouvez baisser la vitesse de transfert en utilisant `--baud 115200`.

### Ecrire le *firmware*

On peut maintenant charger le firmware. On utilise la commande suivante :

```bash
esptool.py --chip esp32 --port /dev/cu.wchusbserial1410 write_flash -z 0x1000 esp32-20180824-v1.9.4-479-g828f771e3.bin
```

N'oubliez pas d'adapter le nom de firmware. Et en moins d'une minute, vous devriez obtenir quelque chose du genre :

```bash
esptool.py v2.5.0
Serial port /dev/cu.wchusbserial1410
Connecting......
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core
MAC: 24:0a:c4:0c:31:1c
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 1053520 bytes to 663112...
Wrote 1053520 bytes (663112 compressed) at 0x00001000 in 59.5 seconds (effective 141.7 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

Pas d'erreur, on peut se connecter sur le shell de notre MicroPython fraîchement installé !

### Se connecter au shell MicroPython

On utilise `screen`pour se connecter en lui donnant le point de montage et la vitesse de transmission (115200 bauds par défaut) :

```bash
screen /dev/cu.wchusbserial1410 115200
```

Et sous vos yeux ébahis :

```bash
I (389) cpu_start: Single core mode
I (389) heap_init: Initializing. RAM available for dynamic allocation:
I (392) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (398) heap_init: At 3FFC4F48 len 0001B0B8 (108 KiB): DRAM
I (405) heap_init: At 3FFE0440 len 00003BC0 (14 KiB): D/IRAM
I (411) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (417) heap_init: At 40091448 len 0000EBB8 (58 KiB): IRAM
I (424) cpu_start: Pro cpu start user code
I (218) cpu_start: Starting scheduler on PRO CPU.
OSError: [Errno 2] ENOENT
MicroPython v1.9.4-479-g828f771e3 on 2018-08-21; ESP32 module with ESP32
Type "help()" for more information.
>>>
```

Félicitations ! 🤩

## Premier test

évidement, comme tout tuto sur de l'embarqué qui se respecte, on va faire clignoter une LED. Si vous avez déjà touché à l'Arduino, vous allez voir comme c'est similaire mais en plus simple grâce à Python.

### Principe

Il est assez simple. Il va falloir savoir sur quel PIN notre LED est connecté (on va trouver ce genre d'information dans la *datasheet* de la carte), comment la faire changer de niveau (bas = 0 = éteint, haut = 1 = allumé) puis trouver quelle fonction nous permet d'attendre entre chaque changement de niveau. Let's go ! ⚙️⚙️⚙️

### Datasheet

Un schéma explicatif et des informations sur la carte sont disponible ici [Olimex Esp32 Gateway](https://docs.zerynth.com/latest/official/board.zerynth.olimex_esp32gateway/docs/index.html). Une image valant mille mots :
![Oh le beau schéma](https://docs.zerynth.com/latest/_images/Olimex_ESP32_gateway_pin_comm.jpg)

On peut voir la LED en haut à gauche puis on la retrouve sur les GPIO comme étant connecté à la broche `D33` (le D est pour *digital* donc numérique).

### Faire changer d'état à une broche

Il y a un module spécifique pour cela : `machine` qui contient une fonction `Pin`. On peut ainsi définir une broche et son sens (c'est à dire si elle en sortie ou en entrée). Une LED est une sortie, on peut donc la définir ainsi :

```python
from machine import Pin

led = Pin(33, Pin.OUT)
```

On pourra faire changer son état grâce à la méthode `value()` de notre LED (qui est du type `Pin`) avec `led.value(1)` pour un état haut et `led.value(0)` pour un état bas.

Pour attendre entre les deux états, nous avons besoins d'un `sleep()`. Ici vous le trouverez dans la librairie `utime` (le `u` est pour micro). On l'utilise ainsi :

```python
from utime import sleep_ms

sleep_ms(500)
```

### Assemblage du tout

On a du coup le code suivant :

```python
from machine import Pin
from utime import sleep_ms

led = Pin(33, Pin.OUT)

while True:
  led.value(1)
  sleep_ms(500)
  led.value(0)
  sleep_ms(500)
```

En copiant/collant ligne par ligne dans `screen`, vous pouvez tester ce code. Mais il y plus facile.

### Utiliser les fichiers

Dans votre session MicroPython, vous pouvez taper le code suivant pour voir les fichiers présents par défaut sur l'ESP32 :

```bash
>>> import os
>>> os.listdir()
['boot.py']
```

Il n'y qu'un seul fichier. On va regarder son contenu.

#### Lister les fichiers

Sortez de votre session de `screen` pour utiliser l'outil `ampy` d'Adafruit. Sans être dans une session de shell (elle doit être fermée sous peine d'erreur), cet outil permet de récupérer la liste des fichiers présents :

```bash
ampy --port /dev/cu.wchusbserial1410 --baud 115200 -d 2 ls
boot.py
```

L'option `--port`est pour notre point de montage, `--baud` pour la vitesse et `-d` pour ajouter un délai. Sans ce délai, j'avais toujours des erreurs. Cette dernière option ne sera peut-être pas nécessaire pour vous, à tester.

Le retour est notre liste de fichier, qui est bien identique à ce que l'on a obtenu dans le shell python.

##### Simplifier ampy

Si vous faites un `ampy --help`, vous pouvez voir que les options peuvent être remplacées par des variables de shell. Ce que je vais faire ici pour me simplifier la tâche. Selon la doc, je peux donc faire (je suis dans un shell `zsh`, à adapter au votre) :

```bash
export AMPY_PORT=/dev/cu.wchusbserial1410
export AMPY_BAUD=115200
export AMPY_DELAY=2
```

Ce qui simplifie ma commande par : `ampy ls`. C'est pas merveilleux ? 🤗

#### Récupérer un fichier

Maintenant que l'on a configurer `ampy`, rien de plus simple :

```bash
ampy get boot.py > boot.py
```

On notera la redirection de flux vers un fichier. En effet, par défaut ampy écrit le résultat directement dans le shell. On peu alors examiner le contenu de ce fichier :

```python
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
```

Hey ! Que du code commenté ! Remplaçons le par notre code écrit plus haut pour faire clignoter notre LED. Une fois le fichier enregistré, nous allons pouvoir le pousser sur notre carte.

#### Uploader un fichier

On utilise l'option `put` de `ampy`, ce qui nous donne :

```bash
ampy put boot.py
```

On fait alors un `reset`de la carte *via* le bouton `RST1`et .... Magie !!! 🧙‍♂️

Si vous vous connectez avec `screen`, vous remarquerez que vous n'avez pas de shell. En effet, notre programme ne termine jamais, il ne rend donc pas la main. Pour revenir au shell, supprimez le `boot.py`de la carte puis réuploadez en un vide.

## Conclusion

Vous, cette "petite" introduction est terminée, j'espère qu'elle vous sera utile et que vous avez appris / eu envie de tester MicroPython !

N'hésitez pas à me faire part de vos commentaires, pour ma part je vais poursuivre mes tests au fil du temps.

Ciao !!
