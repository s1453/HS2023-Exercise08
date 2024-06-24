#!/bin/bash

# Get the name of the current shell
current_shell=$(ps -p $$ -o comm=)

# Check if the current shell is not bash
if [ "$current_shell" != "bash" ]; then
    echo "This script must be run in the Bash shell."
    echo "Please run it using 'bash submit.sh' or make it executable and run './submit.sh'."
    exit 1
fi

# Check if inside a Git repository
function is_git_repository() {
    dir=$(pwd)
    while [ "$dir" != '/' ]; do
        if [ -d "$dir/.git" ]; then
            return 0
        fi
        dir=$(dirname "$dir")
    done
    return 1
}

if ! is_git_repository; then
    echo "This script must be run inside a Git repository."
    exit 1
fi

# Prompt for the email address
read -p "Enter your email address: " email

# Trim and convert the email to lowercase
email=$(echo "$email" | xargs | tr '[:upper:]' '[:lower:]')

# Generate a SHA256 hash of the email using OpenSSL
hash=$(echo -n "$email" | openssl dgst -sha256 | cut -d ' ' -f2)

# Create the submissions directory if it doesn't exist
directory="./submissions"
if [ ! -d "$directory" ]; then
    mkdir "$directory"
fi

# Create a file with the hash as the filename
touch "$directory/$hash.txt"

echo "File created with hash: $hash"
