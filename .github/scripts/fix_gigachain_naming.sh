#!/bin/bash

# Function to perform the replacement while skipping text inside curly braces
replace_text() {
  awk '{
    # Initialize variables
    skip=0
    output=""

    # Iterate through each character
    for(i=1; i<=length($0); i++) {
      char=substr($0, i, 1)
      
      # Toggle skip mode if we encounter curly braces
      if(char == "{") {
        skip++
      }
      if(char == "}") {
        skip--
      }

      # Perform replacements only if not in skip mode
      if(skip == 0) {
        if(match(substr($0, i), /\<lang\>/)) {
          output = output "giga"
          i += 3  # Skip ahead by length of "lang"
        } else if(match(substr($0, i), /\<Lang\>/)) {
          output = output "Giga"
          i += 3  # Skip ahead by length of "Lang"
        } else {
          output = output char
        }
      } else {
        output = output char
      }
    }
    
    print output
  }' "$1"
}

# Find all .toml files in the current directory and subdirectories
find . -type f -name '*.toml' | while read -r file; do
  # Call the replace_text function and save to a temporary file
  replace_text "$file" > "${file}.tmp"
  
  # Move the temporary file to replace the original file
  mv "${file}.tmp" "$file"
done

echo "Replacements completed in all .toml files, except within curly braces."
