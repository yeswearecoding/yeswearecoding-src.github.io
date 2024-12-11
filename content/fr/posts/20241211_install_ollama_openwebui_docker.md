---
title: "Installer Ollama et OpenWebUI sous Ubuntu 24.04 avec un GPU NVIDIA RTX3060"
slug: install_ollama_openwebui_ubuntu_nvidia
date: 2024-12-11T08:38:45+01:00
draft: false
---

Dans le cadre d’un projet personnel, je me suis équipé d’un GPU NVIDIA (une RTX 3060) afin de pouvoir faire tourner convenablement des modèles de LLM en local.

Pour utiliser facilement différent modèle, je m’appuie sur OpenWebUI (avec Ollama) ; comme l’installation peut être un peu épique, je récapitule les différentes étapes ici.

![Image designed by author](/img/llm-desktop.png)

## Configuration utilisée

Dans mon PC, j'ai :

- OS : Ubuntu 24.04 LTS ([Page officielle](https://ubuntu.com/download/desktop))
- GPU : [NVIDIA RTX 3060](https://amzn.to/3D4dDuc) (lien affilié)
- CPU : [AMD Ryzen 7 5700G](https://amzn.to/4gnUvq5) (lien affilié)
- RAM : 52 Go
- Stockage : [Samsung SSD 990 EVO 1TB](https://amzn.to/3D9ASmO) (lien affilié)

Ce qui permet de faire tourner correctement (une trentaine de *tokens/s*) des modèles de `14B`.

## Installation des drivers Nvidia

Il y a plusieurs méthodes, j’ai utilisé celle du site d’Ubuntu : [NVIDIA drivers installation](https://ubuntu.com/server/docs/nvidia-drivers-installation#p-97843-the-recommended-way-ubuntu-drivers-tool)

En résumé, on fait :

```
sudo ubuntu-drivers list
sudo ubuntu-drivers install
```

Puis on vérifie avec `nvidia-smi` . On doit obtenir quelque chose de ce style :

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.120                Driver Version: 550.120        CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3060        Off |   00000000:01:00.0  On |                  N/A |
|  0%   39C    P8             10W /  170W |     664MiB /  12288MiB |      1%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2909      G   /usr/lib/xorg/Xorg                            281MiB |
|    0   N/A  N/A      3245      G   /usr/bin/gnome-shell                          138MiB |
|    0   N/A  N/A     20152      G   ...onEnabled --variations-seed-version        140MiB |
+-----------------------------------------------------------------------------------------+
```

## Installation de Docker avec support des GPU NVIDIA

Pas de difficultés particulières, il faut bien suivre les docs (et ne pas oublier de redémarrer son PC après l’installation du toolkit NVIDIA).

### Docker

On suit la documentation officielle. J’ai choisi la méthode avec les dépôts `apt` : [install-using-the-repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) . Et on oublie pas le _post-installation_ : [linux-postinstall/](https://docs.docker.com/engine/install/linux-postinstall/) (pour éviter de faire un `sudo` à chaque commande Docker).

### NVIDIA Container Toolkit

Idem que précédemment, j’ai utilisé la documentation officielle avec `apt` : [install-guide.html#installing-with-apt](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt) pour installer le _Toolkit_. 

Puis on configuration Docker : [install-guide.html#configuring-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker)

On passe à l’étape de vérification afin de voir que Docker peut bien utiliser le GPU : [running-a-sample-workload](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html#running-a-sample-workload).

On devrait obtenir quelque chose qui ressemble à ça :

```
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
                                                                                                     
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.120                Driver Version: 550.120        CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3060        Off |   00000000:01:00.0  On |                  N/A |
|  0%   43C    P8             12W /  170W |     625MiB /  12288MiB |     31%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
+-----------------------------------------------------------------------------------------+
```

## Ollama et OpenWebUI dans docker-compose

On arrive presque au bout !

Pour gérer facilement Docker (dans un réseau local), j’aime bien utiliser [Portainer](https://docs.portainer.io/start/install-ce/server/docker/linux). Mais on peut aussi le faire sous Vim évidemment, je ne suis pas sectaire.

Pour écrire mon docker-compose.yaml, j’ai utilisé l’exemple d’OpenWebUI : [docker-compose.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.yaml). 

Pour que Docker puisse utiliser le GPU, je me suis basé sur cet exemple-ci : [docker-compose.gpu.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.gpu.yaml).

Ce qui donne :

  

```
services:
  ollama:
    volumes:
      - ollama:/root/.ollama
    container_name: ollama
    pull_policy: always
    tty: true
    restart: unless-stopped
    image: ollama/ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities:
                - gpu

  open-webui:
    build:
      context: .
      args:
        OLLAMA_BASE_URL: '/ollama'
      dockerfile: Dockerfile
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    volumes:
      - open-webui:/app/backend/data
    depends_on:
      - ollama
    ports:
      - 3000:8080
    environment:
      - 'OLLAMA_BASE_URL=http://ollama:11434'
      - 'WEBUI_SECRET_KEY='
    extra_hosts:
      - host.docker.internal:host-gateway
    restart: unless-stopped

volumes:
  ollama: {}
  open-webui: {}
```


Voilà pour une installation de base, pour une utilisation simple (n’allez pas me mettre ça en prod dans cet état, malheureux !!).

N’hésitez pas à me faire part de vos remarques et bon chat avec vos LLM :-)
