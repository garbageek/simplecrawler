"""
Useful functions for crawling and parsing
"""

from urllib.parse import urlsplit, urlparse, urljoin, urldefrag
from bs4 import BeautifulSoup as bs


def get_domain(url):
    """ Return domain name from any URL.
    For example from "http://domain.com/blog/page.html"
    function returns "domain.com"
    """
    return urlparse(url).netloc


def get_links(pagesource, baseurl=None):
    """ Return links set from html page source.
    baseurl parameter should be provided if you wnat to convert
    relative urls to absolute
    """
    soup = bs(pagesource, "lxml")
    soupLinks = soup.find_all("a", href=True)
    if baseurl:
        links = set(map(lambda link: urljoin(baseurl, link.attrs['href']), soupLinks))
    else:
        links = set(map(lambda link: link.attrs['href'], soupLinks))
    return links
