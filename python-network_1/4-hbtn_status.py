#!/usr/bin/python3
"""Fetches URL status and displays response"""
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
