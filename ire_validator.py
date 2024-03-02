import os
import json
import csv
import re

def check_json_file(file_path, source):
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            return (source, os.path.basename(file_path), "Invalid JSON format", "", "", "", "")

        if not isinstance(data, dict):
            return (source, os.path.basename(file_path), "Contents do not start with '{'", "", "", "", "")

        authors = data.get('authors', '')
        conference = data.get('conference', '')
        title = data.get('title', '')
        year = data.get('year', '')
        keywords = data.get('keywords', [])

        if not authors:
            return (source, os.path.basename(file_path), "No 'authors' listed", conference, title, year, len(keywords), "")

        if conference == 'Not Listed':
            conference_msg = "Not Listed"
        else:
            conference_msg = conference

        if year == 'Not Listed':
            year_msg = "Not Listed"
        else:
            year_msg = year

        if 'keywords' in data and len(data['keywords']) != 5:
            keywords_msg = "Doesn't have 5 keywords"
        else:
            keywords_msg = keywords

        return (source, os.path.basename(file_path), "Valid", conference_msg, title, year_msg, keywords_msg, authors)

def check_json_files_in_directories(base_directory):
    results = []
    for dir_name in os.listdir(base_directory):
        if dir_name.startswith('json_') and os.path.isdir(os.path.join(base_directory, dir_name)):
            source = re.sub(r'^json_(.+)$', r'\1', dir_name)
            directory_path = os.path.join(base_directory, dir_name)
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file.endswith('.json'):
                        file_path = os.path.join(root, file)
                        results.append(check_json_file(file_path, source))

    return results

def write_to_csv(file_path, results):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'File Name', 'Status', 'Conference', 'Title', 'Year', 'Keywords', 'Authors'])
        writer.writerows(results)

# Specify the base directory containing the JSON directories
base_directory = '/Users/dwillis/code/ire-stuff'
output_csv_path = '/Users/dwillis/code/ire-stuff/results.csv'

results = check_json_files_in_directories(base_directory)
write_to_csv(output_csv_path, results)
