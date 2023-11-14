import csv
import hashlib

def create_hash_file(csv_file_path, hash_file_path):
    """
    Read CSV file and calculate hash for each mail adress.
    """
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        hashes = []

        for row in csv_reader:
            # Check if CSV file is as expected
            if len(row) < 4:
                continue

            # Mail adress should be in the fourth column
            email = row[3].strip('"')
            # Calculate SHA256 hash
            email_hash = hashlib.sha256(email.encode()).hexdigest().lower()
            hashes.append(email_hash)

    # Write hash to file
    with open(hash_file_path, 'w', encoding='utf-8') as hash_file:
        for h in hashes:
            hash_file.write(h + '\n')

# Paths
csv_file_path = 'teilnehmer.csv'
hash_file_path = '../hashes.txt'

# Execute
create_hash_file(csv_file_path, hash_file_path)