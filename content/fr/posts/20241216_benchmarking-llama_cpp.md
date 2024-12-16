---
title: "Benchmarking de GPU avec Llama.cpp"
slug: benchmarking-llama-cpp
date: 2024-12-16T17:31:18+01:00
draft: false
ShowToc: true
tocopen: true
---

Après avoir [ajouté un GPU et paramétrer ma configuration](https://www.bittenbypython.com/fr/posts/install_ollama_openwebui_ubuntu_nvidia/), j'ai voulu *benchmarker* ma carte graphique. J'ai utilisé [Llama.cpp](https://github.com/ggerganov/llama.cpp) et je l'ai compilé pour utiliser un GPU NVIDIA. Je récapitule ici les différentes étapes.

![Image designed by author](/img/gpu_benchmarking.png)

## Matériel utilisé

- OS: Ubuntu 24.04 LTS ([Official page](https://ubuntu.com/download/desktop))
- GPU: [NVIDIA RTX 3060](https://amzn.to/3D4dDuc) *(affiliate link)*
- CPU: [AMD Ryzen 7 5700G](https://amzn.to/4gnUvq5) *(affiliate link)*
- RAM: 52 GB
- Storage: [Samsung SSD 990 EVO 1TB](https://amzn.to/3D9ASmO) *(affiliate link)*

## Installer le NVIDIA CUDA Toolkit

Pour compiler `llama.cpp`, on a besoin d'installer le [NVIDIA CUDA Toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#download-the-nvidia-cuda-toolkit). Pas de difficulté particulière, il suffit de suivre la documentation (qui est très bien faite).

Une fois fait, il ne faut pas oublier de paramétrer l’environnement [post installation actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions).

On peut alors vérifier que le *toolkit* est bien installé (avec son compilateur pour GPU) : [samples](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#install-writable-samples). Concrètement on fait :

```sh
git clone https://github.com/NVIDIA/cuda-samples.git  
cd cuda-samples/Samples/1_Utilities/deviceQuery
make
```

Ce qui donne :

```sh
./deviceQuery                                                                                                                                                       
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "NVIDIA GeForce RTX 3060"
  CUDA Driver Version / Runtime Version          12.4 / 12.6
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 12004 MBytes (12587106304 bytes)
  (028) Multiprocessors, (128) CUDA Cores/MP:    3584 CUDA Cores
  GPU Max Clock rate:                            1777 MHz (1.78 GHz)
  Memory Clock rate:                             7501 Mhz
  Memory Bus Width:                              192-bit
  
  [...]

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.4, CUDA Runtime Version = 12.6, NumDevs = 1
Result = PASS
```

(j'ai coupé une partie de la sortie pour rester succint)

On peut alors passer à l'installer de [llama.cpp](https://github.com/ggerganov/llama.cpp).

## Installation de Llama.cpp

On  le trouve ici : [llama.cpp](https://github.com/ggerganov/llama.cpp). Pour les impatients, les étapes sont :

### TL;DR :

- Installer les prérequis
- Récupérer le code
- Compiler avec les options pour GPU NVIDIA

### Prérequis

```sh
⁠sudo apt install cmake
```

### Récupération du code

Que du classique, pas de surprise :

```sh
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```

### Compilation

Le lien vers la documentation pour les autres options : [build](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md).

Sur ma machine :

```sh
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```

C'est un peu long, ça m'a pris **17 minutes 41 secondes** (y'a le temps de prendre un café - ou deux ^^).

## Benchmarking

On peut maintenant passer aux mesures.

### Récupérer des modèles

La subtilité est que *llama.cpp* utilise des modèles au format **GGUF**. On peut en trouver facilement sur [HuggingFace](https://huggingface.co/models?sort=downloads&search=gguf). J'ai trouvé la majorité sur le dépôt de [Bartowski](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main).

### Lancer des tests

Dans le répertoire `llama.cpp/build/bin`, je fais :

```sh
./llama-bench -p 0 -n 512 -m ../../models/gemma2-2b-GGUF/dolphin-2.9.4-gemma2-2b-Q5_K_M.gguf -m ../../models/Meta-Llama-3.1-8B-Instruct/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf -m ../../models/Qwen2.5-Coder-14B-Instruct-GGUF/Qwen2.5-14B-Instruct-Q5_K_M.gguf
```

Ce qui me donne :

```sh
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 3060, compute capability 8.6, VMM: yes
| model                          |       size |     params | backend    | ngl |          test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | ------------: | -------------------: |
| gemma2 2B Q5_K - Medium        |   1.79 GiB |     2.61 B | CUDA       |  99 |         tg512 |        119.00 ± 0.72 |
| llama 8B Q5_K - Medium         |   5.33 GiB |     8.03 B | CUDA       |  99 |         tg512 |         53.01 ± 0.06 |
| qwen2 14B Q5_K - Medium        |   9.78 GiB |    14.77 B | CUDA       |  99 |         tg512 |         28.88 ± 0.03 |
```

A noter que si un modèle dépasse la capacité du GPU, on obtient une erreur `failed to load model 'xxx.gguf'`.

## Conclusion

Avec un GPU NVIDIA RTX3060, il est donc possible d'utiliser des modèles de LLM de 14B (14 milliards de paramètres) avec une quantification du type `Q5_K_M` de façon tout à fait satisfaisante (le même ordre de vitesse de réponse que **ChatGPT 4o**).