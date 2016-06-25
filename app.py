import urllib2
import re

def urlregex(url): #test url syntax
	return re.match("(https://|www)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[.]+", url)

def find_word(word,s): #test if word exisit in string s
	return word in s

def crawl(word,url): #count how much given word exist in url html
	url=url.replace("www.", "http://")
	response = urllib2.urlopen(url)	
	page_source = response.read()
	cpt=0
	if(findword(word,page_source)): cpt=cpt+1
	print(cpt)

def find_urls(s):#find all links
	return re.findall(r'href=[\'"]?([^\'" >]+)', s)
	
		
	#print '\n'.join(urls)

def main():
	word=raw_input("Please enter a word to find: ")
	while True:
		url=raw_input("Please enter a website to start: ")
		if urlregex(url):
			break

	url=url.replace("www.", "http://")
	response = urllib2.urlopen(url)	
	page_source = response.read()
	print(find_word(word,page_source))
	#print(find_urls(page_source))

if __name__ == '__main__':
	main()