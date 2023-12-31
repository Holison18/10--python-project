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

    # return the content of the response
    return response.content

# create a function to parse the XML format of the RSS
def parseXML(rss):
    # create an element tree root object
    root = ET.fromstring(rss)

    # create an empty list for newsitems
    newsitem = []

    # iterate news items
    for item in root.findall('./channel/item'):
        news = {}

        # iterate child element
        for child in item:

            # special checking for namespace object content.media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitem.append(news)

    #return news item list
    return newsitem

# define a topstories function to generate and return news items
def topStories():

    # assign our rss loader function to rss
    rss = loadRSS()

    # parse XML
    newsitems = parseXML(rss)
    return newsitems
