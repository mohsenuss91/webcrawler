import BeautifulSoup
import urllib2
import itertools
import random


class Crawler(object):
    """docstring for Crawler"""

    def __init__(self):

        self.soup = None                                        # Beautiful Soup object
        self.current_page   = "http://www.python.org/"          # Current page's address
        self.links          = set()                             # Queue with every links fetched
        self.visited_links  = set()

        self.counter = 0 # Simple counter for debug purpose

    def open(self):

        # Open url
        print self.counter , ":", self.current_page
        res = urllib2.urlopen(self.current_page)
        html_code = res.read()
        self.visited_links.add(self.current_page) 

        # Fetch every links
        self.soup = BeautifulSoup.BeautifulSoup(html_code)

        page_links = []
        try :
            page_links = itertools.ifilter(  # Only deal with absolute links 
                                            lambda href: 'http://' in href,
                                                ( a.get('href') for a in self.soup.findAll('a') )  )
        except Exception: # Magnificent exception handling
            pass



        # Update links 
        self.links = self.links.union( set(page_links) ) 



        # Choose a random url from non-visited set
        self.current_page = random.sample( self.links.difference(self.visited_links),1)[0]
        self.counter+=1


    def run(self):

        # Crawl 3 webpages (or stop if all url has been fetched)
        while len(self.visited_links) < 3 or (self.visited_links == self.links):
            self.open()

        for link in self.links:
            print link



if __name__ == '__main__':

    C = Crawler()
    C.run()