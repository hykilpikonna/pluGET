"""
Constant values

PLUGETVERSION = current version of pluGET
"""

# constant values
import requests

PLUGETVERSION = "1.7.2"

HTTP = requests.Session()
HTTP.headers = {'user-agent': 'pluGET/1.0'}
