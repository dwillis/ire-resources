import openai
import os
import subprocess

# Specify the directory containing the .txt files
directory_path = "text"

# Define the command to be executed

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        print(filename)
        text_string = open(f"text/{filename}", "r").read()
        # Build the command by substituting the file name into the template
        command = f"cat text/{filename} | ttok -t 4000 | llm --system 'create a json file based on the contents of the text with the following keys: id, authors, conference, year, title, description, keywords. The id should be {filename.replace('.txt','').split('-')[1]}. authors is a list containing individual elements with the following attributes: name, email and affiliation. email and affiliation may be null. The description should be a 1-2 sentence summary of the text. The conference would be either IRE or NICAR. The keywords are a list of no more than 5 terms' > {filename.replace('.txt','.json')}"

        try:
            # Execute the command
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command for {filename}: {e}")
