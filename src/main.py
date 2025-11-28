#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 23:33:04 2025

@author: mortivarus
"""

"""
Goal of this script: help with testing issues with running mods for minecraft.

When issues arise in large modpacks it is not always clear what mod or selection
of mods is responsible. Running the game and enabling/disabling each mod to test
it is time-consuming. Thus this script assists in doing the following:
    - Use binary searching to cut up large modbases into two ever smaller chunks for testing.
    - Make a list of mods and their dependencies based on mcmod.info inside the jar 
    - Make testing of mods easier, and allow for large modpacks to get debugged quicker.



Handlers:
    - jar_handler: what it says on the tin. Converts jar to zip, then extracts the zip to a subfolder and deletes the zip.
    - dependencies_handler: scans through mods folder for jar files, unpacks them,
      extracts dependancy info out of mcmod.info and generates a dependencies.json file.
    - search_handler: TODO



"""

from pathlib import Path
import jar_handler as jh
import os
import string


# root = input("Please enter the minecraft folder root.")
root = "/home/mortivarus/Games/Minecraft/MultiMC/install/instances/ATM6_custom/minecraft/"

# os.chdir(root)

paths = {}
paths["root"] = Path(root)
paths["crash-reports"] = paths["root"].joinpath("crash-reports")
paths["mods"] = paths["root"].joinpath("mods")


crash_reports = paths["crash-reports"].glob("*.txt")
crash_reports_list = sorted([report.name for report in crash_reports])

mods = paths["mods"].glob("*.jar")
mods_list = sorted([mod.name for mod in mods])

num = round(0.5*len(mods_list))
selection = mods_list[:num] 
rest = mods_list[num:]


missing_dependancies = []
with open(paths["crash-reports"].joinpath(crash_reports_list[-1]), 'r') as f:
    for i in f.readlines():
        if "Failure message: Mod" in i:
            value = i.strip()
            # value = i.sub("Failure message:", "")
            missing_dependancies.append(value)
            
            
# Switch for adding or removing '.bak' from mod name to turn it off/on

def mod_switcher(mod_file_name):
    if ".bak" in mod_file_name:
        mod_file_name = mod_file_name.replace(".bak", "")
    else:
        mod_file_name += ".bak"
    
    return mod_file_name


def cleanup(path):
    for file in os.listdir(path):
        os.remove(file)
    return




# Make a list of all mods
# Select half the mods, deactivate the rest
# Make user run the game
# Ask user if game loaded to menu.
# If game did not run, check crash log for missing dependancies. Reactivate missing dependancies, and run again.
# If game did run, close game. Deactivate active mods, and reactivate the other half
# 























