#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""

    try:
        req = requests.post(url, data=({'q': letter}))
        response_json = req.json()

        if response_json:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
