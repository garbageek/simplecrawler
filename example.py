#!/usr/bin/python3

from crawlers import SimpleCrawler

dead_links_spider = SimpleCrawler("http://domain.com/")
print("Starting...")
dead_links_spider.crawler()
print("Finished")
print('\n'.join(dead_links_spider.get_dead_links()))
