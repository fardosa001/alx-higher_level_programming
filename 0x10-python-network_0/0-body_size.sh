#!/usr/bin/bash
# script that takes in a URL, sends a request to that URL,
# displays the size of the body of the response
curl -sI "$1" | grep 'content-length:' | cut -f2 -d' '
