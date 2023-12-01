#!/usr/bin/python3
"""a script that prints the list of last 10 commits from most recent to oldest
use the GitHub API"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    req = requests.get(url)
    listCommits = req.json()
    for commit in listCommits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
