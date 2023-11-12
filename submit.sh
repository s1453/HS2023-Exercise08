#!/bin/bash

# Prompt for the email address
read -p "Enter your email address: " email

# Trim and convert the email to lowercase
email=$(echo $email | xargs | tr '[:upper:]' '[:lower:]')

# Generate a SHA256 hash of the email using OpenSSL
hash=$(echo -n $email | openssl dgst -sha256 | cut -d ' ' -f2)

# Create the submissions directory if it doesn't exist
directory="./submissions"
if [ ! -d "$directory" ]; then
    mkdir "$directory"
fi

# Create a file with the hash as the filename
touch "$directory/$hash.txt"

echo "File created with hash: $hash"
