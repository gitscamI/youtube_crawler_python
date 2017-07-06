import urllib.request, urllib.parse, urllib.error
from os.path import join
import os
from bs4 import BeautifulSoup
import ssl
import pafy
import re
from download import download, getAudioUrl
from changePage import nextPageUrl
from m4a_to_wav import m4aToWav

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

saveDirectory = './Music'

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

song_num = 0
current_page = 1

if not os.path.exists(saveDirectory):
    os.makedirs(saveDirectory)


while(song_num < 100):
    # Download music
    video_urls = getAudioUrl(soup)
    for i in range(len(video_urls)):
        # Every url repeat twice
        if(i % 2 == 1):
            continue
  
        song_num, filename = download(video_urls[i], song_num, saveDirectory)
        # useless url make filename = 0 without saving file
        if(filename != 0):
            m4aToWav(filename, saveDirectory)
            os.remove(filename)
    print('download ok')
    # renew url for next page
    current_page, next_page_url = nextPageUrl(current_page,soup)
    url = next_page_url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('next_page ok')
