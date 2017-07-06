# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

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




def getAudioUrl(soup):
    # Retrieve all of the anchor tags
    tags = soup('a')
    video_urls = []
    for tag in tags:
        x = re.findall('/watch.+', str(tag.get('href', None)))
        if(len(x) > 0):
            video_urls.append(x) 

    # print (video_urls)
    return video_urls


def download(url_list, song_num, saveDirectory):
    url = 'http://youtube.com' + url_list[0]
    try: 
        video = pafy.new(url)
    except Exception as e:
        # print(type(e), str(e))
        filename = 0
        return song_num, filename
    song_num += 1
    audiostreams = video.audiostreams
    audioDownload = 0
    for a in audiostreams:
        # print(a.bitrate, a.extension, a.get_filesize())
        if(a.extension == 'm4a'):
            audioDownload = a
            break
    filename = audioDownload.download(filepath = saveDirectory, quiet = False)
    print(filename)
    return song_num, filename

# Usage for the above two function
def downloadSong(song_num, soup, saveDirectory):
    video_urls = getAudioUrl(soup)
    for i in range(len(video_urls)):
        if(i % 2 == 1):
            continue
 
        song_num, filename = download(video_urls[i], song_num, saveDirectory)
    return song_num

if __name__ == "__main__":
    
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    song_num = 0
    saveDirectory = './Music'
    
    song_num = downloadSong(song_num, soup, saveDirectory)

    print(song_num)
