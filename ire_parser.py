import openai
import os
import subprocess

# Specify the directory containing the .txt files
directory_path = "text"
output_dir = "json_google"

output_files = [f.split('.json')[0] for f in os.listdir(output_dir)]

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt") and filename.split(".txt")[0] not in output_files:
        print(filename)
        text_string = open(f"text/{filename}", "r").read()
        # Build the command by substituting the file name into the template
        try:
            file_id = filename.replace('.txt','').split('-')[1]
        except:
            file_id = filename.replace('.txt','').split('-')[0]
        command = f"cat text/{filename} | ttok -t 4000 | llm -m palm 'You are a helpful assistant that only returns valid JSON objects. Create a json object based on the contents of the text with the following keys: id, authors, conference, year, title, description, keywords. The id should be {file_id}. authors is a list containing individual elements with the following attributes: name, email and affiliation. Do NOT make up any names; leave the name null if none is listed. email and affiliation may be null, but if the text includes the name of a news organization, use that as the affiliation if none appears next to the author name. The description should be a 1-2 sentence summary of the text in direct, simple language. The conference will be either IRE, NICAR or Not Listed. If the year of the event is not clearly identified, the value of year is Not Listed. The keywords are a list of no more than five terms excluding the conference and authors. The response must not be enclosed in any text or formatting' > {output_dir}/{filename.replace('.txt','.json')}"

        try:
            # Execute the command
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command for {filename}: {e}")
