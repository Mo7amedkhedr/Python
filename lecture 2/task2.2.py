#!/usr/bin/python3



import requests
from pprint import pprint
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
pprint(data)