import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_218684.xml'

iter = 0
while iter < 1:
    # address = raw_input('Enter location: ')
    # if len(address) < 1 : break

    # url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', serviceurl
    uh = urllib.urlopen(serviceurl)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    # print data
    tree = ET.fromstring(data)
    results = tree.findall('.//name')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
	
    # print 'lat',lat,'lng',lng
    # print location
    sum = 0
    for item in results:
        print item.text
		# sum += float(item.text)
    iter += 1
print sum