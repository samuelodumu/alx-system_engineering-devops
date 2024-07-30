#!/usr/bin/python3
"""Indents a JSON file (makes it human readable)"""
import json
file_path = trivias.json
with open(file_path, r) as file:
    content = json.load(file)
    file.flush()
