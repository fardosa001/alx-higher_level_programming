#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as response:
        html = response.read()
        utf8_content = html.decode('utf-8')
        print('Body response:')
        print("    - type: {}".format(type(html)))
        print("    - content: {}".format(html))
        print("    - utf8 content: {}".format(utf8_content))
