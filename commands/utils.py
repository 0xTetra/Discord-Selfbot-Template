"""
This file will store every piece of JSON you parse for ease of access in all files,
and other utilitizes you will need.

To import this file in your other files:
    from utils import token, prexix

If you'd like to import every variable in this file:
    from utils import *
"""

import json

token = json.loads(open('config.yml').read())['token']
prefix = json.loads(open('config.yml').read())['prefix']