import requests
import os
from datetime import datetime

API_KEY = os.environ["NEWS_API_KEY"]
PAGE_SIZE = 5
PAGE_NUM = 1

def get_news(term="corona"):
    curDate = datetime.date(datetime.now())
    url = ('http://newsapi.org/v2/everything?'
       'q={}&'
       'from={}&'
       'sortBy=popularity&'
       'pageSize={}&'
       'page={}&'
       'apiKey={}'.format(term, curDate, PAGE_SIZE, PAGE_NUM, API_KEY))
    response = requests.get(url)
    print(response.json())
