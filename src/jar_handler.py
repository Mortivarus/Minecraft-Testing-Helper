#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 21:01:14 2025

@author: mortivarus
"""
from zipfile import ZipFile
import os
import shutil
from pathlib import Path
import tomllib

def check_path(path):    
    path_type = str(type(path))
    is_path = (False, True)["pathlib" in path_type]
    
    if is_path:
        return path
    else:
        print('[INFO] Not a Path object. Converting to one.')
        return Path(path)

def extract_zip(file_path, dest_path):
    print(f"[INFO] Extracting {file_path} to {dest_path}.")
    with ZipFile(file_path, 'r') as zip_file:
        zip_file.extractall(dest_path)
    print("[INFO] Extraction done.")

def extract_jar(file_path, dest_path):
    file_path = check_path(file_path)
    dest_path = check_path(dest_path)
    name = Path(file_path).stem
    zip_path = file_path.with_suffix('.zip')
    print("[INFO] Copying jar to zip for extraction as .zip.")
    shutil.copyfile(file_path, zip_path)
    dest_subfolder = dest_path.joinpath(name)
    os.mkdir(dest_subfolder)
    extract_zip(zip_path, dest_subfolder)
    print("[INFO] Removing temporary zip file.")
    os.remove(zip_path)
    
    print(f"[INFO] Successfully extracted {file_path} to {dest_path}.")
    return

