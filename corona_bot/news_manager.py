import corona_bot.news_api as news
from corona_bot.url_shortener import shorten_url

def get_news() -> str:
    """Gets the updated news on the corona virus and returns the article titles and urls as a message."""
    titleUrlMap = news.get_news()
    for title, url in titleUrlMap.items():
        titleUrlMap[title] = shorten_url(url)
    message = format_message(titleUrlMap)
    print(message)
    return message


def format_message(titleUrlMap:dict()) -> str:
    """Given the mapping of the title to the url, returns a well formatted string of the information"""
    message = ''
    for title, url in titleUrlMap.items():
        message += title + '\n'
        message += url + '\n'
    return message
