# -*- coding: UTF-8 -*-
import urllib2
import re

def read_urls_from_file(fname):
	with open(fname) as f:
		return f.readlines()

def urlregex(url): #test url syntax
	return re.match("(https://|www)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[.]+", url)

def find_word(word,s): #test if word exisit in string s
	return word in s

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
	wor=raw_input("Please enter a word to find: ")

	websites=read_urls_from_file("data/test.txt")#reading websites from a file
	for url in websites:
		url=url.replace("\n", "")
		if urlregex(url):		
			url=url.replace("http://www.", "http://")
			url=url.replace("www.", "http://")			
			print("Reading [{}]").format(url)
			response = urllib2.urlopen(url)
			page_source = response.read()
			if(find_word(wor,page_source)):
				print("\t({}) = = > {}").format(wor,url)
			else:
				print("({}) was not found in [{}]").format(wor,url)				
		else:
			print("Please make sure of [{}] syntax. It must be in [www.******.***] format").format(url)	

if __name__ == '__main__':
	main()