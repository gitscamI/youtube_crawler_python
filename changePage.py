import urllib.request, urllib.parse, urllib.error
from os.path import join
from bs4 import BeautifulSoup
import ssl
import pafy
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
   


def nextPageUrl(current_page, soup):
    next_page_url = 0
    # Retrieve all of the anchor tags

    tags = soup('a')
    for tag in tags:
        x = re.findall('前往第 '+str(current_page+1)+' 頁', str(tag.get('aria-label', None)))
        if(len(x) > 0):
            
            next_page_url_list = re.findall('/results?.+', str(tag.get('href', None)))
            next_page_url = 'https://www.youtube.com' + next_page_url_list[0]
            break
              
    current_page += 1
    return current_page, next_page_url

if __name__ == "__main__":
    saveDirectory = './Music'
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    current_page = 1
    current_page, next_page_url = nextPageUrl(current_page, soup)

    print(next_page_url)



