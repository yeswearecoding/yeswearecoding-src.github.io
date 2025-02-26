---
title: "GPU benchmarking with Llama.cpp"
slug: benchmarking-llama-cpp
categories: [ai, LLM]
date: 2024-12-16T17:31:18+01:00
draft: false
ShowToc: true
tocopen: true
---

After [adding a GPU and configuring my setup](https://www.bittenbypython.com/en/posts/install_ollama_openwebui_ubuntu_nvidia/), I wanted to benchmark my graphics card. I used [Llama.cpp](https://github.com/ggerganov/llama.cpp) and compiled it to leverage an NVIDIA GPU. Here, I summarize the steps I followed.

![Image designed by author](/img/gpu_benchmarking.png)

## Hardware Used

- OS: Ubuntu 24.04 LTS ([Official page](https://ubuntu.com/download/desktop))
- GPU: [NVIDIA RTX 3060](https://amzn.to/3OVHDvb) *(affiliate link)*
- CPU: [AMD Ryzen 7 5700G](https://amzn.to/3ZWVOGD) *(affiliate link)*
- RAM: 52 GB
- Storage: [Samsung SSD 990 EVO 1TB](https://amzn.to/4gF9b3Q) *(affiliate link)*

## Installing the NVIDIA CUDA Toolkit

To compile `llama.cpp`, you need to install the [NVIDIA CUDA Toolkit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#download-the-nvidia-cuda-toolkit). The process is straightforward—just follow the well-documented guide.

Once installed, don't forget to configure the environment as described in the [post-installation actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions).

You can verify the installation of the toolkit (and the GPU compiler) by running the provided [samples](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#install-writable-samples). Specifically, execute:

```sh
git clone https://github.com/NVIDIA/cuda-samples.git  
cd cuda-samples/Samples/1_Utilities/deviceQuery
make
```
This should produce:

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

(I trimmed the output for brevity.)

Now, you can proceed to install llama.cpp.

## Installing Llama.cpp

The project is available here: [llama.cpp](https://github.com/ggerganov/llama.cpp). For the impatient, here are the steps:

### TL;DR

- Install prerequisites
- Retrieve the code
- Compile with NVIDIA GPU options

### Prerequisites

```sh
⁠sudo apt install cmake
```

### Retrieving the Code

Simple and straightforward:

```sh
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```

### Compilation

Refer to the documentation for additional options: [build](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md).

On my machine, the steps were:

```sh
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```

The compilation took 17 minutes and 41 seconds—long enough for one (or two) coffee breaks. 😊

## Benchmarking

Now it's time to run benchmarks.

### Retrieving Models

A key point is that llama.cpp requires models in the GGUF format. You can find such models easily on [HuggingFace](https://huggingface.co/models?sort=downloads&search=gguf). I found most of them in [Bartowski's repository](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main).

### Running Tests

In the `llama.cpp/build/bin directory`, I ran:

```sh
./llama-bench -p 0 -n 512 -m ../../models/gemma2-2b-GGUF/dolphin-2.9.4-gemma2-2b-Q5_K_M.gguf -m ../../models/Meta-Llama-3.1-8B-Instruct/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf -m ../../models/Qwen2.5-Coder-14B-Instruct-GGUF/Qwen2.5-14B-Instruct-Q5_K_M.gguf
```

This produced:

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

Note: If a model exceeds the GPU's capacity, you will encounter an error: `failed to load model 'xxx.gguf'`.

## Conclusion

With an NVIDIA RTX3060 GPU, it is therefore possible to use LLM models of 14B (14 billion parameters) with quantization of the `Q5_K_M` type in a completely satisfactory way (the same order of speed of response as **ChatGPT 4o**).