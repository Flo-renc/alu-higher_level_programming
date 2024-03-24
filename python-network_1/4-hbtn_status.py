#!/usr/bin/python3
"""
Module to fetch the status of a URL and display the response body.
"""

import requests

def fetch_status(url):
    """Fetches the status of a URL and displays the response body.

    Args:
        url (str): The URL to fetch the status from.

    Raises:
        RequestException: If an error occurs while fetching the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print(f"Body response:\n{response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_status(url)
