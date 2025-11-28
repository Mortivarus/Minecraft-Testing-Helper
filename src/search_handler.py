#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 19:35:43 2025

@author: mortivarus
"""

"""
Module uses binary search to figure out in which group the faulty mod is.
"""
import re

def check_answer_regex(answer):
    match answer:
        case a if re.fullmatch(r"y(es)?", a, flags=re.IGNORECASE):
            return True
        case a if re.fullmatch(r"n(o)?", a, flags=re.IGNORECASE):
            return False
        case _:
            return None

def ask_user_yes_no():
    # Ask user if game worked
    result = check_answer_regex(input("Did the game run correctly? Y/N\n"))
    
    # If answer is not in the options. 
    while result == None:
        print("Invalid answer, please try again.")
        result = check_answer_regex(input("Did the game run correctly? Y/N\n"))
    
    return result

def split_mods_list(mods_list):
    middle = round(0.5*len(mods_list))
    groups = {
        "group_1": mods_list[:middle],
        "group_2": mods_list[middle:]
        }
    return groups


def search_cycle(mods_list):
    if len(mods_list<=1):
        print(f"[WARNING] Modlist too short. Exiting.")
    # Split mods up into two groups
    groups = split_mods_list(mods_list)
    # 
    
    # Select group 1
    
    # Check dependencies for group 1, add dependencies
    
    # Run group 1
    print("[INFO] Please run the game now.\n")
    result_1 = ask_user_yes_no()
    
    # Select group 2
        
    # Check dependencies for group 2, add dependencies
        
    # Run group 2
    print("[INFO] Please run the game now.\n")
    # Ask user if game worked
    result_2 = ask_user_yes_no()
    #     return
    
    
        
        
search_cycler("herp")
    

    
    
    
