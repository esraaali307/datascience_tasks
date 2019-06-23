# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:12:26 2019

@author: A
"""
# the technique used for this problem is web crawling which starts with lists of urls and visits them recusively according to set of policies and here is example for this technique 
import urllib2
#import ssl
from lib.crawler import Crawler
import scrapy
import time
import urllib

import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Wikipedia"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    article_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link
def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2)
#class BrickSetSpider(scrapy.Spider):
   # name = 'brick_spider'
    #start_urls = ['https://en.wikipedia.org/wiki/Wikipedia']
#url = input ('enter url : ')
#no_links = int (input('enter position of philosophy')) #number of links between first link and philosophy 
#counter = 0
#def getphilo (normal_link):
    #if counter != position:
   # f = urllib2.urlopen(normal_link)
   # print(normal_link)
    
