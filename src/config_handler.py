#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 19:05:26 2025

@author: mortivarus
"""

from configparser import ConfigParser
from pathlib import Path

def read_config(path):
    # Create a ConfigParser object
    config = ConfigParser()

    # Read the configuration file
    config.read(path)
    
    return config
