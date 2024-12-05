import os

# Path to the folder
folder_path = '/Users/dmondal/Documents/langid/data/raw_data/bodo'

output_file = 'bodo.txt'

# Extract file names without the .wav extension
wav_files = [os.path.splitext(file)[0] for file in os.listdir(folder_path) if file.endswith('.wav')]

# Write names to the output file
with open(output_file, 'w') as file:
    for name in wav_files:
        file.write(name + '\n')

print(f"Extracted names of .wav files saved to '{output_file}'.")