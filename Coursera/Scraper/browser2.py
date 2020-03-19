import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print mysock

######## SIC
#mysock.connect(('www.sic.gov.co',80))
#mysock.send('GET http://serviciospub.sic.gov.co/~oparra/serv_57/externas/datospatente.php HTTP/1.0\n\n')

######### Python 4 informatics
mysock.connect(('www.py4inf.com',80))
#mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0
picture = "";
while True:
    data = mysock.recv(5120)
    if (len(data) < 1) : break
    # time.sleep(0.25)
    count = count + len(data)
    print len(data), count
    picture = picture + data
    

mysock.close()
#Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n")
print ' Header length', pos
print picture [:pos]

#Skip past the header and save the picture data
picture = picture [pos+4:]
fhand = open("stuff.jpg","w")
fhand.write(picture)
fhand.close()