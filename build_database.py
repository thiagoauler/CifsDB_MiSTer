#!/usr/bin/python3

import argparse
import hashlib
import json
import os
import time

def build_rom_database(base_directory):
    db_files = {}
    
    # Walking a directory tree and printing the names of the directories and files
    for dirpath, dirnames, files in os.walk(base_directory):
        for file_name in files:
            file_path = os.path.join(dirpath, file_name)
            file_size = os.stat(file_path).st_size
            file_hash = md5(file_path)
            file_path = file_path.replace(base_directory, '')
            
            db_game = {
                "hash": file_hash,
                "overwrite": "true",
                "size": file_size,
                "url": "file:///media/fat/cifs" + file_path
            }
            
            db_files["games" + file_path] = db_game
    return db_files

def md5(file_path):
    h = hashlib.md5()

    # hash the file itself
    with open(file_path, "rb", buffering=0) as f:
        # use a small buffer to compute hash to
        # avoid memory overload
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.hexdigest()

parser = argparse.ArgumentParser(description='A simple script that generates a custom database for a shared folder to MiSTer.')
parser.add_argument('folder_path', help='shared folder to create custom database')
args = parser.parse_args()

base_directory = args.folder_path

if not os.path.exists(base_directory):
    print('The provided path does not exist.')
    exit()

if not os.path.isdir(base_directory):
    print('The provided path is not a folder.')
    exit()

db_files = build_rom_database(base_directory)

db = {
    "base_files_url": "",
    "db_files": [],
    "db_id": "cifs_db",
    "default_options": {},
    "files": db_files,
    "folders": {
        "games": {}
    },
    "timestamp": int(time.time()),
    "zips": {}
}

print(json.dumps(db))