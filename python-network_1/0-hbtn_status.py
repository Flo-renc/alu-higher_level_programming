#!/usr/bin/python3
"""This script fetches "https://alu-intranet.hbtn.io/statushave to use urlib module/library"""


import urllib.request
def fetch_url(url):
    """
    Fetches the content of a URL using urllib.

    Args:
        url (str): The URL to fetch.

    Returns:
        bytes: The content of the response.

    Raises:
        URLError: If there was an error fetching the URL.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
    return content

def display_response_body(content):
    """
    Displays the body of the response.

    Args:
        content (bytes): The content of the response.
    """
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))

if __name__ == "__main__":
    url = 'http://0.0.0.0:5050/status'
    response_content = fetch_url(url)
    display_response_body(response_content)
