#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as response:
        html = response.read()
        utf8_content = html.decode('utf-8')
        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(html)))
        print('\t- content: {_content}'.format(_content=html))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
