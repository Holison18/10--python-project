# This program is a python code to scrap news headlines from a URL

import requests
import xml.etree.ElementTree as ET

# url of new rss feed
RSS_FEED_URL = "https://www.ghanaiantimes.com.gh/feed/"

# create a function to load rss
def loadRSS():
    '''
    This is a utility function to load RSS feee
    '''
    # create an HTTP request response object
    response = requests.get(RSS_FEED_URL)