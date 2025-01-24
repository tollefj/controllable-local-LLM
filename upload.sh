#!/bin/bash
jupyter-book build .
scp -r _build/html/* ntnu:~/public_html/books/local-llm
