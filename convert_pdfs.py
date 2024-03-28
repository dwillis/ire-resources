import os
import subprocess

# Input and output directories
input_dir = 'pdfs'
output_dir = 'text'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over PDF files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.txt')

        # Check if the output file already exists
        if not os.path.exists(output_file_path):
            # Call pdftotext shell command
            subprocess.run(['pdftotext', input_file_path, output_file_path])

            print(f"Converted {filename} to text.")
        else:
            print(f"Skipped {filename} as text file already exists.")
