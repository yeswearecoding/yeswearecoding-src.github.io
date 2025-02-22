---
title: "Install Ollama and OpenWebUI on Ubuntu 24.04 with an NVIDIA RTX3060 GPU"
slug: install_ollama_openwebui_ubuntu_nvidia
categories: [ia, LLM]
date: 2024-12-11T08:38:45+01:00
draft: false
---

As part of a personal project, I equipped myself with an NVIDIA GPU (an RTX 3060) to properly run LLM models locally.

To easily use different models, I rely on OpenWebUI (with Ollama). Since the installation can be a bit of an adventure, I’m summarizing the steps here.

![Image designed by author](/img/llm-desktop.png)

## Configuration Used

On my PC, I have:

- OS: Ubuntu 24.04 LTS ([Official page](https://ubuntu.com/download/desktop))
- GPU: [NVIDIA RTX 3060](https://amzn.to/3OVHDvb) *(affiliate link)*
- CPU: [AMD Ryzen 7 5700G](https://amzn.to/3ZWVOGD) *(affiliate link)*
- RAM: 52 GB
- Storage: [Samsung SSD 990 EVO 1TB](https://amzn.to/4gF9b3Q) *(affiliate link)*

This setup allows me to properly run `14B` models (around thirty *tokens/s*).

## Installing the Nvidia Drivers

There are several methods; I used the one from the Ubuntu site: [NVIDIA drivers installation](https://ubuntu.com/server/docs/nvidia-drivers-installation#p-97843-the-recommended-way-ubuntu-drivers-tool)

In summary, run:

```
sudo ubuntu-drivers list 
sudo ubuntu-drivers install
```

Then verify with `nvidia-smi`. You should get something like this:

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

## Installing Docker with NVIDIA GPU Support

No particular difficulties here; just follow the documentation (and don’t forget to reboot your PC after installing the NVIDIA toolkit).

### Docker

Follow the official documentation. I chose the method with `apt` repositories: [install-using-the-repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository). Don’t forget the post-installation steps: [linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall/) (to avoid using `sudo` for each Docker command).

### NVIDIA Container Toolkit

Same as before, I used the official documentation with `apt`: [install-guide.html#installing-with-apt](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt) to install the Toolkit.

Then configure Docker: [install-guide.html#configuring-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker)

Proceed to the verification step to ensure Docker can indeed use the GPU: [running-a-sample-workload](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html#running-a-sample-workload).

You should get something like this:

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

## Ollama and OpenWebUI in docker-compose

We’re almost done!

To easily manage Docker (on a local network), I like to use [Portainer](https://docs.portainer.io/start/install-ce/server/docker/linux). But you can also do it with Vim, of course, I’m not picky.

To write my `docker-compose.yaml`, I used the OpenWebUI example: [docker-compose.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.yaml).

To allow Docker to use the GPU, I relied on this example: [docker-compose.gpu.yaml](https://github.com/open-webui/open-webui/blob/main/docker-compose.gpu.yaml).

Which gives:

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

That’s a basic installation for simple use (don’t you dare put this into production as is!).

Feel free to share your feedback and enjoy chatting with your LLMs :-)
