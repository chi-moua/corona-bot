import requests
import os
from datetime import datetime

API_KEY = os.environ["NEWS_API_KEY"]
PAGE_SIZE = 5
PAGE_NUM = 1

ARTICLES = 'articles'
REQUEST_URL = 'http://newsapi.org/v2/everything?'
TITLE = 'title'
URL = 'url'

def get_news(term="corona") -> dict:
    curDate = datetime.date(datetime.now())
    params = {
        'q': term,
        'from': curDate,
        'sortBy':'popularity',
        'pageSize': PAGE_SIZE,
        'page': PAGE_NUM,
        'apiKey': API_KEY
    }
    response = requests.get(REQUEST_URL, params=params)
    responseDict = response.json()
    titleUrlMapping = get_title_url_mapping(responseDict[ARTICLES])
    print(titleUrlMapping)
    print(response.json())
    return titleUrlMapping

def get_title_url_mapping(articles:list) -> dict:
    titleUrlMapping = dict()
    for article in articles:
        titleUrlMapping[article[TITLE]] = article[URL]
    return titleUrlMapping
