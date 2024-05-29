#!/bin/bash

DIRECTORY=$1

# Find all .toml files in the current directory and subdirectories
find "$DIRECTORY" -type f -name '*.toml' | while read -r file; do
  # Use sed to perform the replacements and create a temporary file
  sed -e 's/\blang\b/giga/g' -e 's/\bLang\b/Giga/g' "$file" > "${file}.tmp"
  
  # Move the temporary file to replace the original file
  mv "${file}.tmp" "$file"
done

echo "Replacements completed in all .toml files."
