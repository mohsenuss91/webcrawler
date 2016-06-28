from BeautifulSoup import BeautifulSoup, SoupStrainer
import re
import urllib2

doc = urllib2.urlopen("http://somesite.com").read()
links = SoupStrainer('a', href=re.compile(r'^test'))
soup = [str(elm) for elm in BeautifulSoup(doc, parseOnlyThese=links)]
for elm in soup:
    print elm