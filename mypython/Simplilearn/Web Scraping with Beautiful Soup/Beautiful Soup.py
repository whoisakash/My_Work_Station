'''Problem Statement
Scrape the Simplilearn website page using Beautiful Soup library and perform the following
tasks:
1. View and print the Simplilearn web page's content in a good format
2. View the head and title
3. Print all the href links present in the Simplilearn web page'''

from bs4 import BeautifulSoup
import requests

# url for web scraping
url = "https://www.simplilearn.com"

# access the url with request object
result = requests.get(url)

# scrape the web page content
webpage = result.content

# create a soup object for parsing web page using html parser
sl_soup = BeautifulSoup(webpage, "html.parser")

# close the result object
result.close()

# view the content of the soup object
# print(sl_soup.contents)

# view the head of the soup object
# print(sl_soup.head)
# print(sl_soup.title)

# find all the links present on the web page
for href in sl_soup.findall("a", href=True):
    print(href["href"])