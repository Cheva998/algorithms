import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_218688.json'

web_info = urllib.urlopen(url)
data = web_info.read()
info = json.loads(data)
print 'User count:', len(info)

suma = 0
for item in info['comments']:
    # print 'name', item['name']
    # print 'count', type(item['count'])
    suma += item['count']
print suma