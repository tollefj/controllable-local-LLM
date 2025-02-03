#!/bin/bash
sudo systemctl stop ollama.service
OLLAMA_MAX_LOADED_MODELS=1 OLLAMA_NUM_PARALLEL=1 ollama serve
