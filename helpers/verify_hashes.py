import os
import sys

def verify_submissions(hash_file_path, directory_path):
    """
    Check whether the hashes in the file name of the files in the specified folder
    appear in the hashes.txt file.
    """
    # Read hashes file
    with open(hash_file_path, 'r', encoding='utf-8') as file:
        valid_hashes = {line.strip() for line in file}

     # Check each file in the specified folder
    for filename in os.listdir(directory_path):
        # Ignore files starting with a dot (e.g. .gitkeep)
        if filename.startswith('.'):
            continue

        file_hash = filename.split('.')[0]  # ignore file extensions
        if file_hash.lower() not in valid_hashes:
            print(f"Found invalid submission: {filename}")
            return 1 

    print("All submissions are valid.")
    return 0  # Alle Hashes stimmen überein

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python verify_hashes_in_directory.py [hash_file_path] [directory_path]")
        sys.exit(1)

    hash_file_path = sys.argv[1]
    directory_path = sys.argv[2]
    result = verify_submissions(hash_file_path, directory_path)
    sys.exit(result)
