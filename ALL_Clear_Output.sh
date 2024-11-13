#!/bin/bash

# This script clears all outputs from Jupyter notebooks in the current directory and its subdirectories.

# Check if 'jupyter nbconvert' is installed
if ! command -v jupyter &> /dev/null; then
    echo "Error: jupyter nbconvert is not installed. Please install Jupyter Notebook (e.g., 'pip install notebook') and try again."
    exit 1
fi

# Find all .ipynb files in the current directory and subdirectories
for notebook in $(find . -name "*.ipynb"); do
    echo "Clearing outputs for $notebook..."
    jupyter nbconvert --clear-output --inplace "$notebook"
done

echo "All notebook outputs have been cleared."

# Instructions:
# To use this script:
# 1. Give it executable permissions by running:
#    chmod +x clear_outputs.sh
# 2. Then, execute it with:
#    ./clear_outputs.sh
#
# This will remove all cell outputs (including graphs and visualizations) 
# from every Jupyter notebook (.ipynb file) in the repository.
