# Models

In general, I would always recommend you to use the GGUF quants. Will provide much more "bang for the buck" than the original weights.

Recommended quants are `Q4_K_M`, `Q5_K_M` and `Q6_K`

## Accessing them in Ollama

As you saw previously, the template is quite straightforward:

```bash
ollama run hc.co/<user>/<model_id>:<quant>
```

## Recommended models

- Gemma-2 (9B/27B)
  - <https://huggingface.co/bartowski/gemma-2-9b-it-GGUF>
  - <https://huggingface.co/bartowski/gemma-2-27b-it-GGUF>
- Phi-4 (14b)
  - <https://huggingface.co/unsloth/phi-4-GGUF>
- Llama-3.2 (3B/1B)
  - <https://huggingface.co/collections/unsloth/llama-32-66f46afde4ca573864321a22>
  - <https://huggingface.co/unsloth/Llama-3.2-1B-Instruct>
  - <https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-GGUF>
- Mistral Small 3 (2501) (24B)
  - <https://huggingface.co/bartowski/Mistral-Small-24B-Instruct-2501-GGUF>