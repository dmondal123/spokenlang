
#!/bin/bash

# Number of threads
nt=$3

# Extract the base filename without the extension
fname=$(basename "$1" .txt)

# Use the filename to create a folder name
folder="$fname"

# Define root and save directory
root=$2
save_dir="$root/raw_data/$folder"

# Create the save directory if it doesn't exist
if [ ! -d "$save_dir" ]; then
    mkdir -p "$save_dir"
fi

# Download audio from YouTube links in the input file
cat "$1" | xargs -I '{}' -P "$nt" yt-dlp -f "bestaudio/best" -ciw \
  -o "$save_dir/%(id)s.%(ext)s" \
  --extract-audio --audio-format wav --audio-quality 0 --no-playlist https://youtu.be/{} \
  --ppa "ffmpeg:-ac 1 -ar 16000"

# Process the downloaded files using VAD, SNR filter, and chunking
python vad.py "$root/raw_data/" "$root/data_refined/" "$folder" &&
python snr_filter.py "$root/data_refined/" "$folder" "$root/snr_rejected/" &&
python chunking.py "$root/data_refined/$folder"



