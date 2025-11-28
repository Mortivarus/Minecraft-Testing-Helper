#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 00:04:59 2025

@author: mortivarus
"""

import jar_handler as jh
from pathlib import Path
import shutil
import os
import json
import multithread_handler as mh
import time

"""

Dependancy handler should scan all mods in folder, extract dependancies and 
generate a json as profile. Dependencies are often described in mcmod.info,
hence this file needs to be extracted and imported from the jar file.

Steps:
    - find all files in mods folder ending with '.jar'
    - extract jar mods to output folder, under their own folder name
    - check jar folder for '.info' file, often called 'mcmod.info'
    - import .info file, check if it is version 1 or 2. Version 1 has the format as a dict within a one-item list, version 2 is a dict within a list within a dict
    - dependencies are named under keys 'dependencies/dependancies' and 'requiredMods'
    - remove any forge related dependancies
    - generate a hashtable for modids and mod file names
    - generate a dict with mod ids and the subsequent dependancy files. Omit any without dependencies.
    - export a json with said dict.
"""
mods_path = Path("../mods")
output_path = "../output"


def cleanup(path):
    path = jh.check_path(path)
    for file in os.listdir(path):
        file = path.joinpath(file)
        shutil.rmtreefile   
    print(f"[INFO] {path} cleared")
    return


def extract_mods(mods_path, output_path):
    mods = []
    mods_path = jh.check_path(mods_path)
    for file in os.listdir(mods_path):
        if Path(file).suffix == ".jar":
            full_path = mods_path.joinpath(file)
            mods.append(mods_path)
            
            try:
                mh.multithread(jh.extract_jar, full_path, output_path)
            except:
                print("[WARNING] File could not be extracted. Skipping.")
                continue
    

def scan_mods(mods_path):
    mods = []
    mods_path = jh.check_path(mods_path)
    for file in os.listdir(mods_path):
        if Path(file).suffix == ".jar":
            full_path = mods_path.joinpath(file)
            mods.append(full_path)
    return mods



def process_mod_dependencies(mod_path, output_path="../output"):
    mod_path = jh.check_path(mod_path)
    output_path = jh.check_path(output_path)
    mod_name = mod_path.stem
    extracted_mod_path = output_path.joinpath(mod_name)
    
    if extracted_mod_path.exists():
        print(f"[WARNING] Folder already exists at {extracted_mod_path}.")
        return
    
    try:
        jh.extract_jar(mod_path, output_path)
    except:
        print(f"[WARNING] Can't extract {mod_name}.")
        return
    
    shutil.rmtree(extracted_mod_path)
    
    return
    

# extract_mods(mods_path)

# cleanup(output_path)


mods = scan_mods(mods_path)

process_mod_dependencies(mods[5])

# print("All Files extracted.")

# config_files = []

def get_info_file_paths(output_path):
    output_path = jh.check_path(output_path)
    info_file_paths_list = []
    for folder in os.listdir(output_path):
        folder_path = output_path.joinpath(folder)
        
        for file in os.listdir(folder_path):
            file_path = folder_path.joinpath(file)
            
            if file_path.suffix == ".info":
                info_file_paths_list.append(file_path)
    
    return info_file_paths_list


def get_info_file():
    return




# config_files_content = []
# for file in config_files:
#     if file.exists():
#         try:    
#             with open(file, 'r') as file2:
#                 data = json.load(file2)
#                 config_files_content.append(data)
#         except:
#             # print(f"Couldn't load {file2.name}")
#             continue

# herp = [i[0] for i in config_files_content if type(i) is list]

# flerp = [i for i in config_files_content if type(i) is dict]

dep_names_set = {'dependencies', 'dependancies', 'requiredMods'}

# derp = [{i["modid"]:i["dependencies"]} for i in herp if "dependencies" in i]

# zerp = [{i["modid"]:i["dependancies"]} for i in herp if "dependancies" in i]

# dep_list = []
# for i in dep_names_set:
#     print(i)


# test = []

# for i in herp:
#     for j in i.keys():
#         if "dep" in j:
#             test.append(j)
            
# test = set(test)



