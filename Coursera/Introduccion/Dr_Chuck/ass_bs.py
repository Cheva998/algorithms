import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_218687.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print type(tag.contents[0])
    nume = int(tag.contents[0])
    print type(nume)
    #print 'Attrs:',tag.attrs
    count += int(tag.contents[0])
print count