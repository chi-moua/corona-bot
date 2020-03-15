import requests
import os
from datetime import datetime

API_KEY = os.environ["NEWS_API_KEY"]
PAGE_SIZE = 5
PAGE_NUM = 1

ARTICLES = 'articles'
URL = 'url'
TITLE = 'title'

def get_news(term="corona") -> dict:
    curDate = datetime.date(datetime.now())
    url = ('http://newsapi.org/v2/everything?'
       'q={}&'
       'from={}&'
       'sortBy=popularity&'
       'pageSize={}&'
       'page={}&'
       'apiKey={}'.format(term, curDate, PAGE_SIZE, PAGE_NUM, API_KEY))
    response = requests.get(url)
    responseDict = response.json()
    titleUrlMapping = get_title_url_mapping(responseDict[ARTICLES])
    print(response.json())
    return titleUrlMapping

def get_title_url_mapping(articles:list) -> dict:
    titleUrlMapping = dict()
    for article in articles:
        titleUrlMapping[article[TITLE]] = article[URL]
    return titleUrlMapping