#!/bin/bash

# Install virtualenv package
pip install virtualenv

# Create and activate virtual environment named "venv"
python -m virtualenv venv
source ./server/venv/bin/activate

# Install Python packages from requirements.txt
pip install -r ./server/requirements.txt
