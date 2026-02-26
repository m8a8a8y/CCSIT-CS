import os
import subprocess

# This script is meant to be run by root to backup user uploads.

UPLOAD_DIR = "/app/uploads"
BACKUP_DIR = "/var/backups"

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

print(f"Starting backup of {UPLOAD_DIR}...")

# Change directory to uploads
os.chdir(UPLOAD_DIR)

# VULNERABLE: Using wildcard with shell=True allows argument injection if filenames contain flags
# e.g., --checkpoint=1 --checkpoint-action=exec=sh
subprocess.call("tar -czf /var/backups/uploads.tar.gz *", shell=True)

print("Backup completed successfully.")
