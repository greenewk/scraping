from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())

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


def getTitle(bs):
    # Gets Title of a BS object
    try:
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

def wikiGetLinks(article_name):
    """
    Accepts the name of a Wikipedia article, eg '/wiki/Kevin_Bacon'
    Returns all links to other Wikipedia articles within it
    """

    article_url = (f'http://en.wikipedia.org/{article_name}')
    bs = make_soup(article_url)
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
                                        href = re.compile(
                                            '^(/wiki/)((?!:).)*$'
                                        ))
def crawl_wiki(first_article):
    """
    Start with a Wikipedia article name, eg '/wiki/Kevin_Bacon'
    and navigate recursively, navigating to a random link on the
    page and then from that page and so on
    """

    links = wikiGetLinks(first_article)
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs['href']
        print(new_article)
        links = wikiGetLinks(new_article)
