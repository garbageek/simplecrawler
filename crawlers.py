"""
Module contains web crawler(s) with main purpose - grab dead links
"""

import requests
from crawlerhelpers import get_domain, get_links


class SimpleCrawler(object):
    """Simple Synchronous (Blocking) Crawler Class for parsing urls from page source and return them as list of strings
    Arguments:
    baseurl -- base url for converting relative urls to absolute (string)
    page -- page source, string type
    """

    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.basedomain = get_domain(self.baseurl)
        self.links = []
        self.deadlinks = []

    def get_page_links(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            self.deadlinks.append(url)
            print("URL: '{}' added to deadlinks".format(url))
            return None
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)
            return None
        return get_links(r.text, self.baseurl)

    def crawler(self, url=None):
        """Recursive Blocking crawler"""
        if not url:
            url = self.baseurl
        links = self.get_page_links(url)
        if links:
            for link in links:
                if get_domain(link) == self.basedomain:
                    if link not in self.links:
                        self.links.append(link)
                        self.crawler(link)

    def get_dead_links(self):
        return self.deadlinks
