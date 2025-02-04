# Setup

1. Download [ollama](https://ollama.com/download) for easy serving of models. It supports most operating systems.
2. Follow the instructions and install `ollama`. **Do not download any models yet.**
   - `ollama` enables a CLI for running models (soon!).
3. If the application doesn't start up properly, type `ollama serve` in your terminal.
   - If it's already running, you will see an error message like `Error: listen tcp 127.0.0.1:11434: bind: address already in use`.

For local hosting, we usually prefer to run _quantized_ GGUF models, named after the developer of the format, Georgi Gerganov.

- Georgi is also the main developer of [whisper.cpp](https://github.com/ggerganov/whisper.cpp) and [llama.cpp](https://github.com/ggerganov/llama.cpp), C++ systems to run AST and LLMs respectively.
- Nearly all LLM applications, including `ollama`, are built on top of compiled binaries from llama.cpp.

## GGUF

- GGUF is a format that allows quantization of models.
- Typical PyTorch models (or similar) can be converted to a .GGUF format.
- These are lower bit representations of the full-precision weights used when training the networks.
  - For example, from FP16 (half-precision) to a ~5 bit representation, commonly denoted by the "Q5" suffix.
    - Libraries like PyTorch train with FP32, but we've moved towards mixed-precision which combines FP32 and FP16:
      - FP16: weights/activations
      - FP32: gradients during backpropagation for numerical stability.
- This can reduce a 70B model (140GB) to 20-30GB while still being fairly usable.

```{image} ../assets/gguf-bytes.png
:alt: gguf-bytes
:class: bg-primary mb-1
:align: center
```

Here's a list of some quantized versions of the Llama-3.3 70B model:

```{image} ../assets/gguf-download.png
:alt: gguf-download
:class: bg-primary mb-1
:align: center
```

## Getting Started with a Model

Let's begin with `llama-3.2 1B` - a small 1B model just to test out our system.

- Typically, there are devoted people out there who download the original models and quantize them with Llama.cpp, so we can download the premade GGUF file.
  - One of the most active ones is the user `bartowski` on Hugging Face.
    - If you don't know of Hugging Face, it's basically the GitHub of AI models and datasets.
- Path: <https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/blob/main/Llama-3.2-1B-Instruct-Q6_K.gguf>
- You can click "Use this model" -> `ollama` to create a runnable command:

```{image} ../assets/huggingface-menu.png
:alt: hf dl menu.png
:class: bg-primary mb-1
:align: center
```

Run the following command to use the model:

```bash
ollama run hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q6_K_L
```

This is the 6-bit version of the highest quality. It's only 1.1GB, so let's start with that.

The output of the run command:

```{image} ../assets/ollama-cli.png
:alt: ollama-cli
:class: bg-primary mb-1
:align: center
```

However, we're not interested in talking to it through the terminal; we want to process outputs in our code, i.e., we need an API!
