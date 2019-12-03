from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def make_soup(url):
    # Returns a BeautifulSoup object of a webpage
    try: 
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found.')
    else:
        return BeautifulSoup(html.read(), 'html.parser')


def getTitle(soup):
    # Gets Title of a BS object
    try:
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
