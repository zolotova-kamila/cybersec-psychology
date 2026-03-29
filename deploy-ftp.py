#!/usr/bin/env python3
"""FTP Deployment Script for pozitiv-psychology.ru"""

import os
import sys
import ftplib
from pathlib import Path

# FTP credentials
FTP_HOST = "vh278.timeweb.ru"
FTP_USER = "cu48621"
FTP_PASS = "tfCq8P4a"
FTP_REMOTE_PATH = "/pozitiv-psychology.ru/public_html"

# Files to exclude from upload
EXCLUDE = {
    '.git', '.gitignore', 'deploy-*.sh', 'deploy-*.ps1', 'deploy-ftp.py',
    'lftp.zip', '__pycache__', '.env', '.vscode', '.idea',
    '*.md', 'AGENTS.md'
}

def should_upload(filename):
    """Check if file should be uploaded"""
    for pattern in EXCLUDE:
        if pattern.startswith('*'):
            if filename.endswith(pattern[1:]):
                return False
        elif filename == pattern or filename.startswith(pattern.replace('*', '')):
            return False
    return True

def upload_directory(ftp, local_path, remote_path):
    """Upload directory recursively"""
    local_path = Path(local_path)
    
    for item in local_path.iterdir():
        if not should_upload(item.name):
            continue
            
        remote_item_path = f"{remote_path}/{item.name}"
        
        if item.is_dir():
            # Create directory if doesn't exist
            try:
                ftp.mkd(item.name)
            except ftplib.error_perm:
                pass  # Directory already exists
            
            # Change to directory
            ftp.cwd(item.name)
            upload_directory(ftp, item, remote_item_path)
            ftp.cwd('..')
        else:
            # Upload file
            print(f"Uploading: {item.relative_to(Path.cwd())}")
            try:
                with open(item, 'rb') as f:
                    ftp.storbinary(f'STOR {item.name}', f)
            except Exception as e:
                print(f"Error uploading {item}: {e}")

def main():
    print("=" * 50)
    print("FTP Deployment to pozitiv-psychology.ru")
    print("=" * 50)
    
    try:
        print(f"\nConnecting to {FTP_HOST}...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        
        print("Connected!")
        print(f"Current directory: {ftp.pwd()}")
        
        # Change to remote path
        try:
            ftp.cwd(FTP_REMOTE_PATH)
        except ftplib.error_perm:
            print(f"Creating remote directory: {FTP_REMOTE_PATH}")
            ftp.mkd(FTP_REMOTE_PATH)
            ftp.cwd(FTP_REMOTE_PATH)
        
        print(f"\nUploading files to {FTP_REMOTE_PATH}...")
        print("-" * 50)
        
        upload_directory(ftp, Path.cwd(), FTP_REMOTE_PATH)
        
        print("-" * 50)
        print("\nDEPLOY COMPLETED!")
        print(f"\nCheck site: https://pozitiv-psychology.ru/")
        
        ftp.quit()
        
    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
