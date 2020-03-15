import requests
import os

RAPIDLY_API_KEY = os.environ["REBRANDLY_API_KEY"]
PATH = 'https://api.rebrandly.com/v1/links'

""" $ curl 'https://api.rebrandly.com/v1/links' \
-X POST \
-H 'apikey: YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d \
'{
  "title": "What is Rebrandly",
  "slashtag": "video",
  "destination": "https://www.youtube.com/watch?v=3VmtibKpmXI"
}'
// slashtag and title are optional """

def shorten_url(url:str):
    payload = {
    'apikey': RAPIDLY_API_KEY,
    'Content-Type': 'application/json',
    'destination': url
    }
    result = requests.post(PATH, json=payload)
    print(result.json())

shorten_url('https://requests.readthedocs.io/en/master/user/quickstart/#more-complicated-post-requests')
