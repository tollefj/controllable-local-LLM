# Local and Controllable LLMs

The book is live at <https://tollefj.folk.ntnu.no/books/local-llm>

## Jupyter-book

- build and serve it:

`jupyter-book build .`

`python -m http.server --directory _build/html`

Alternatively, use sphinx to serve it:

1. `pip install sphinx-autobuild`
2. `jupyter-book config sphinx .`
3. `sphinx-autobuild . _build/html -b html`
