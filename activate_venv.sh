#!/bin/bash

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
    echo "The virtual environment 'venv' does not exist. Create it first with: python3 -m venv venv"
    exit 1
fi

# Activate the virtual environment (for bash/zsh)
source venv/bin/activate

echo "Virtual environment 'venv' activated."
echo "You can now install packages or run your scripts."
