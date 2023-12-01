#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    req = requests.post(url, data={'q': letter})

    try:
        res_json = req.json()

        if res_json:
            print("[{}] {}".format(res_json.get('id'), res_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
