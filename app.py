#!/usr/bin/python3
# -*- coding: UTF-8 -*-
try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request
import re

def read_urls_from_file(fname): #reading lines from a file
	with open(fname) as f:
		return f.readlines()

def urlregex(url): #test url syntax
	return re.match("(https://|www)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[.]+", url)

def find_word(word,s): #test if word exisit in string s
	return word.encode() in s

def crawl(word,url): #count how much given word exist in url html
	url=url.replace("http://www.", "http://")
	url=url.replace("www.", "http://")
	response = urllib2.urlopen(url)	
	page_source = response.read()
	cpt=0
	if(find_word(word,page_source)): cpt=cpt+1
	return cpt!=0

def find_urls(s):#find all links
	return re.findall(r'href=[\'"]?([^\'" >]+)', s)


def main():
	wor=input("Please enter a word to find: ")

	websites=read_urls_from_file("data/algerian_univ.txt")#reading websites from a file
	for url in websites:
		url=url.replace("\n", "")
		if urlregex(url):		
			url=url.replace("http://www.", "http://")
			url=url.replace("www.", "http://www.")			
			print("\nReading [%s]" % url)
			req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			response = urlopen(req)
			page_source = response.read()
			if(find_word(wor,page_source)):
				print("\t(%s) = = > %s" % (wor,url))
			else:
				print("(%s) was not found in [%s]" % (wor,url))			
		else:
			print("Please make sure of [%s] syntax. It must be in [www.******.***] format" % url)	

if __name__ == '__main__':
	main()