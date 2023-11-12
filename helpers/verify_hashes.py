import os

def verify_hashes_in_directory(hash_file_path, directory_path):
    """
    Check whether the hashes in the file name of the files in the specified folder
    appear in the hashes.txt file.
    """
    # Read hashes file
    with open(hash_file_path, 'r', encoding='utf-8') as file:
        hashes = {line.strip() for line in file}

    # Check each file in the specified folder
    for filename in os.listdir(directory_path):
        file_hash = filename.split('.')[0]  # ignore file extensions
        if file_hash not in hashes:
            return 1  # terminate script if there is an unknown hash

    return 0 

