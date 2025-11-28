#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 22:45:20 2025

@author: mortivarus
"""
from concurrent.futures import ThreadPoolExecutor
import os

def multithread(function, *args, max_workers=min(32, os.cpu_count() + 4)):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future = executor.submit(function, *args)
        return future.result()
    
