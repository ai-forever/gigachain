#!/bin/bash

# Loop through all .toml files in the current directory
for file in *.toml; do
  # Check if there are no .toml files
  if [ ! -e "$file" ]; then
    echo "No .toml files found in the current directory."
    exit 1
  fi

  # Use sed to perform the replacements and create a temporary file
  sed -e 's/\blang\b/giga/g' -e 's/\bLang\b/Giga/g' "$file" > "${file}.tmp"
  
  # Move the temporary file to replace the original file
  mv "${file}.tmp" "$file"
done

echo "Replacements completed in all .toml files."
