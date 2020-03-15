import requests
import os

RAPIDLY_API_KEY = os.environ["REBRANDLY_API_KEY"]
PATH = 'https://api.rebrandly.com/v1/links'
SHORT_URL = 'shortURL'

def shorten_url(url:str):
    payload = {
    'apikey': RAPIDLY_API_KEY,
    'Content-Type': 'application/json',
    'destination': url
    }
    result = requests.post(PATH, json=payload)
    resultDict = result.json()
    return resultDict[SHORT_URL]

