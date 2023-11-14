import csv
import hashlib
import os

def hash_email(email):
    """Generate a SHA256 hash for the given email."""
    return hashlib.sha256(email.lower().strip().encode()).hexdigest()

def evaluate_submissions(teilnehmer_csv, submissions_dir, output_csv):
    """
    Generate a CSV file with name, firstname, email for all valid submissions.
    Also, report unknown submissions in the submissions directory.
    """
    # Get hashes of files in submissions directory, ignoring files starting with '.'
    submission_hashes = {filename.split('.')[0].lower() for filename in os.listdir(submissions_dir) if not filename.startswith('.')}

    known_hashes = set()
    with open(teilnehmer_csv, 'r', encoding='utf-8') as infile, \
         open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header
        writer.writerow(['Name', 'Firstname', 'Email'])

        for row in reader:
            if len(row) < 4:  # Skip if row of the teilnehmer.csv file is not valid
                print(f"Invalid row found: {row}")
                continue

            name, firstname, email = row[1].strip('"'), row[2].strip('"'), row[3].strip('"')
            email_hash = hash_email(email).lower()
            known_hashes.add(email_hash)

            if email_hash in submission_hashes:
                writer.writerow([name, firstname, email])

    # Report unknown submissions
    unknown_submissions = submission_hashes - known_hashes
    for unknown_hash in unknown_submissions:
        print(f"Unknown submission: {unknown_hash}")

# Example usage
teilnehmer_csv = 'teilnehmer.csv'
submissions_dir = '../submissions'
output_csv = 'valid_submissions.csv'

evaluate_submissions(teilnehmer_csv, submissions_dir, output_csv)
