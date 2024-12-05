
#!/bin/bash

# Ensure the first two arguments are provided
if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: bash process_data.sh </path/to/download> <num_of_threads>"
    exit 1
fi

# Iterate over each .txt file in ../urls/
for l in ../urls/*.txt; do
    # Extract the filename without the extension
    filename=$(basename "$l" .txt)

    # Create the corresponding directory for storing data
    mkdir -p "$filename"

    # Call dw_util.sh with the required arguments
    bash dw_util.sh "$l" "$1" "$2" # Pass the URL file, download path, and number of threads
done
