#!/usr/bin/pyhon3
""" class module """
import json


def load_from_json_file(filename):
    """ load from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
