# Check if inside a Git repository
function IsGitRepository {
    $currentDir = Get-Location
    while ($currentDir -ne [System.IO.Path]::GetPathRoot($currentDir)) {
        if (Test-Path (Join-Path $currentDir '.git')) {
            return $true
        }
        $currentDir = [System.IO.DirectoryInfo]$currentDir.Parent
    }
    return $false
}

if (-not (IsGitRepository)) {
    Write-Host "This script must be run inside a Git repository."
    Exit
}

# Prompt for the email address
$email = Read-Host -Prompt "Enter your email address"

# Trim and convert the email to lowercase
$email = $email.Trim().ToLower()

# Generate a SHA256 hash of the email
$hasher = [System.Security.Cryptography.SHA256]::Create()
$hashedBytes = $hasher.ComputeHash([Text.Encoding]::UTF8.GetBytes($email))
$hash = [BitConverter]::ToString($hashedBytes) -replace '-', ''

# Create the submissions directory if it doesn't exist
$directory = ".\submissions"
if (-not (Test-Path $directory)) {
    New-Item -ItemType Directory -Path $directory
}

# Create a file with the hash as the filename
$file = Join-Path $directory "$hash.txt"
New-Item -Path $file -ItemType File

Write-Host "File created with hash: $hash"
