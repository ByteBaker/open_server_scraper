from datetime import datetime
from scraper_lib import *

__title__ = 'open_server_scraper'
__version__ = '0.1.0'
__author__ = "Shraddha Kishan Tripathi"
__license__ = 'GPL v3.0'

FILES_COUNT = dict()
TIMESTAMP = lambda : datetime.now().strftime('%d-%m-%Y %I:%m:%S') 


def descriptive_log(url=None):
	if url is None:
		MESSAGE = 'Total ' + str(sum(FILES_COUNT.values())) + ' files were found.\n\n'
		LOG_FILE.write(MESSAGE)
		print(MESSAGE.strip())
		for extension in FILES_COUNT:
			MESSAGE = extension.upper() + ' - ' + str(FILES_COUNT.get(extension, 0)) + ' files.\n'
			LOG_FILE.write(MESSAGE)
			print(MESSAGE.strip())
	else:
		MESSAGE = 'Open server scraper by Shraddha Kishan\n'
		MESSAGE += 'Traversing: ' + unquote(url)
		MESSAGE += '\nStarted at ' + TIMESTAMP()
		MESSAGE += '\n=====================================\n\n'
		LOG_FILE.write(MESSAGE)

def add_log(filename=None, url=None):
	if filename is not None:
		MESSAGE = TIMESTAMP() + ' | FILE: ' + unquote(filename) + '\nAT: ' + unquote(url) + '\n\n'
		LOG_FILE.write(MESSAGE)
		print('FILE:', unquote(filename),'\n')
	else:
		MESSAGE = TIMESTAMP() + ' | ' + 'PAGE: ' + unquote(url) + '\n\n'
		LOG_FILE.write(MESSAGE)
		print(MESSAGE.strip())

def count_files(file_name):
	try:
		extension = file_name.split('.')[-1]
		FILES_COUNT[unquote(extension)] = FILES_COUNT.get(unquote(extension),0) + 1
		return
	except:
		return

def traverse(url):
	is_a_page, file_name = is_page(url)
	if not is_a_page:
		OUTPUT_FILE.write(unquote(file_name) + ',' + unquote(url) + '\n')
		count_files(unquote(file_name))
		add_log(filename=file_name, url=url)
		return
	else:
		add_log(filename=file_name, url=url)
		nextSet = getUrlSet(url, contentMaker(url))
		if len(nextSet) == 1:
			return
		else:
			for new_url in nextSet:
				if is_parent(new_url, url):
					continue
				elif len(new_url.split('?')) > 1:
					continue
				else:
					traverse(new_url)

""" Below is the driver function """
def web_scraper():
	BASE_URL = input("Enter url: ")

	OUTPUT_FILE_NAME = 'index_' + BASE_URL.split('://')[1] + '.csv'
	OUTPUT_FILE_NAME = OUTPUT_FILE_NAME.replace('/','_').replace(':','_')
	global OUTPUT_FILE
	OUTPUT_FILE = open(OUTPUT_FILE_NAME,'w')
	global LOG_FILE
	LOG_FILE = open('SCRAPER_LOG.txt', 'w')
	descriptive_log(url=BASE_URL)

	if not BASE_URL.endswith('/'):
		BASE_URL += '/'
	traverse(BASE_URL)

	descriptive_log()
	OUTPUT_FILE.close()
	LOG_FILE.close()




