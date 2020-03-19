import urllib
from BeautifulSoup import *
import json
import ssl

url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Bryce.html"
posit = 18
repet = 7

for idx in range(1,repet + 1):
    #SErver certification##############
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
	######
    # html = urllib.urlopen(url).read()
	
    soup = BeautifulSoup(data)
    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
         
        # print tag.contents[0]
        count += 1
        if count == posit:
            url = tag.get('href', None)
            name = tag.contents[0]
            break
    # print "\n", "Other round"
print name