import os

def compare_directories(directory1, directory2):
    files1 = set(os.listdir(directory1))
    files2 = set(os.listdir(directory2))

    files_only_in_dir1 = files1 - files2

    return files_only_in_dir1

def write_to_file(file_path, unique_files):
    with open(file_path, 'w') as f:
        for file in unique_files:
            f.write(file + '\n')

def main():
    directory1 = 'pdfs'
    directory2 = 'text'
    output_file = 'pdfs_with_no_text.txt'

    unique_files = compare_directories(directory1, directory2)

    write_to_file(output_file, unique_files)

if __name__ == "__main__":
    main()
