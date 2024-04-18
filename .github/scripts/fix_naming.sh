#!/bin/bash

# Check if the file path is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_toml_file>"
    exit 1
fi

# Assign the provided file path to a variable
toml_file="$1"

# Check if the file exists
if [ ! -f "$toml_file" ]; then
    echo "Error: File '$toml_file' not found."
    exit 1
fi

# Use sed to replace "Langchain" with "Gigachain" in lines
sed -i -E '/packages = \[/,/^\s*\]/! s/langchain/gigachain/' "$toml_file"
