# Local and Controllable LLMs

## Jupyter-book

- build and serve it:

`jupyter-book build .`

`python -m http.server --directory _build/html`

Alternatively, use sphinx to serve it:

1. `pip install sphinx-autobuild`
2. `jupyter-book config sphinx .`
3. `sphinx-autobuild . _build/html -b html`

- finally, share it on github pages:

`jupyter-book build . && ghp-import -n -p -f _build/html`
