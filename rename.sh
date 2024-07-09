#!/bin/bash

# Google forms appends " - Name" to the filename, but we want to import them as Python modules

cd submissions || { echo "No directory 'submissions'"; exit 1; }

for file in *.py; do
  if [[ "$file" == *" "* ]]; then
    new_filename=$(echo "$file" | cut -d' ' -f1).py
    mv "$file" "$new_filename"
    echo "Renamed '$file' to '$new_filename'"
  fi
done
