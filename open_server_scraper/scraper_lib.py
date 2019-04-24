from bs4 import BeautifulSoup as bs
import urllib3 as ul3
import re

def unquote(text):
  return re.compile('%([0-9a-fA-F]{2})',re.M).sub(lambda m: chr(int(m.group(1),16)), text)


# Checks if the URL is a page or file
def is_page(url):
	filename = url.split('/')[-1]
	if len(filename) == 0:
		return True, None
	else:
		return False, filename

def is_parent(url, parent):
	if url[6:].find('//') != -1:
		return True
	if url.endswith('/'):
		url = url[:-1]
	if parent == url[:-2]:
		return True
	else:
		return False

# Returns the BeautifulSoup object instance of a URL
def contentMaker(url):
	try:
		httpNode = ul3.PoolManager()
		response = httpNode.request('GET',url)
		return (bs(response.data,'lxml'))
	except:
		return None


def getUrlSet(url=None, soup=None):
	if soup is None:
		return soup
	tags = soup.find_all('a')
	urlSet = set()
	for tag in tags:
		relative_url = tag.get('href')
		if relative_url == '/':
			continue
		else:
			urlSet.add(url + relative_url)
	return urlSet

