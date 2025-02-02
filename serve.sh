#!/bin/bash
jupyter-book build .
python -m http.server --directory _build/html
