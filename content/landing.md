# Local and Controllable LLMs

This is a simple guide for hosting your own local LLM through an API (`ollama` w/`llama.cpp`) to access it by different helper functions, including the necessary basics of tool use and data creation.

The goal here is to use smaller models that fit on our laptops to perform useful tasks, something you may have thought to be requiring cloud services or APIs from anthropic or openai.

Most of the tasks in real-world applications and sciency stuff requires _control_ over what kind of outputs we get from a model.

Let's say you want to generate a synthetic dataset. You expect a certain amount of columns for each data point. What if you want to create a recipe website? You would like to structure the raw text as a specific and predictable format. Same same, but different.

Today there's hundreds of available libraries to solve this, but they often contain more than they need to.

What we want:

1. A model small enough for a laptop (`<16GB`) served through an API
2. A system for handling and orchestrating responses
3. Something useful you can use in your master's thesis, perhaps!

```{image} ../assets/local-llama.png
:alt: local-llama
:class: bg-primary mb-1
:align: center
:width: 400px
```

<!-- caption -->
<p style="text-align: center;">a local llama (probably)</p>
<!-- add a coding style text below: -->
<code style="text-align: center;">Generated with FLUX.1 [schnell] 8-bit, 6.5GB on a macbook.</code>
<code style="text-align: center;">Prompt: a portrait pencil sketch of a cool llama with sunglasses, wearing a sweater saying "LOCAL and CONTROLLABLE", minimalist, impressionism, negative space</code>
