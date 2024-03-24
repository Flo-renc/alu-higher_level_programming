#!/usr/bin/python3
"""Fetches URL status and displays response"""
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
