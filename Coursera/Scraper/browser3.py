import urllib
from BeautifulSoup import *
url = "http://www.dr-chuck.com/page1.htm"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)

