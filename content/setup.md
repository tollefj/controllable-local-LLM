# Setup

- download [ollama](https://ollama.com/download) for easy serving of models, supports most operating systems.
- follow the instructions and "install". **do not download any models yet.**
  - `ollama` enables a CLI for running models (soon!)
- in case the application doesn't start up properly, type `ollama serve` in your terminal.

  - if it's already running, you will see something like `Error: listen tcp 127.0.0.1:11434: bind: address already in use`

- for local hosting, we usually prefer to run _quantized_ GGUF models, named after the developer of the format Georgi Gerganov.
  - Georgi is also the main developer of [whisper.cpp](https://github.com/ggerganov/whisper.cpp) and [llama.cpp](https://github.com/ggerganov/llama.cpp), C++ systems to run AST and LLMs respectively.
  - nearly all llm-applications, including `ollama`, is built on top of compiled binaries from llama.cpp.

## GGUF

- a format that allows quantization of models.
- typical pytorch models (or similar) can be converted to a .GGUF format.
- these are lower bit representations of the full-precision weights used when training the networks
  - e.g., from FP16 (half-precision) to a ~5 bit representation, commonly denoted by the "Q5" suffix.
    - libraries like PyTorch train with FP32, but we've moved towards mixed-precision which combines FP32 and FP16:
      - FP16: weights/activations
      - FP32: gradients during backprop: numerical stability
- can reduce a 70B model (140GB!!!) to 20-30GB while still being fairly usable.

```{image} ../assets/gguf-bytes.png
:alt: gguf-bytes
:class: bg-primary mb-1
:align: center
```

Here's a list of some quants of the Llama-3.3 70B model:

```{image} ../assets/gguf-download.png
:alt: gguf-download
:class: bg-primary mb-1
:align: center
```

## getting started with a model

- Let's begin with `llama-3.2 1B` - a small 1B model just to test out our system
- typically, there are devoted people out there that download the original models and quantize them with Llama.cpp, such that we can download the premade GGUF file.
  - one of the most active ones is the user `bartowski` on huggingface.
    - if you don't know of huggingface, it's basically the github of AI models and datasets
- path: <https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/blob/main/Llama-3.2-1B-Instruct-Q6_K.gguf>
- you can click "use this model" -> `ollama` that creates a runnable command:

```{image} ../assets/huggingface-menu.png
:alt: hf dl menu.png
:class: bg-primary mb-1
:align: center
```

`ollama run hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q6_K_L`

- this is the 6-bit version of highest quality. It's only 1.1GB, so let's start with that.

the output of the run command:

```{image} ../assets/ollama-cli.png
:alt: hf dl menu.png
:class: bg-primary mb-1
:align: center
```

buuuut... we're not interested in talking to it through the terminal, we want to process outputs in our code, i.e., we need an API!
