#!/bin/bash

echo "Removing virtual environment"
rm -rf venv

echo "Cleaning all Python cache files"
find . -type d -name "__pycache__" -exec rm -rf {} +
echo "Done.Thank you for playing. Cya ^_^ "


