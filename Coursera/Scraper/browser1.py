############################
###### Python 3 #########
############################

import time
import urllib.request
#
#
#######SIC
#fhan = urllib.request.urlopen('http://serviciospub.sic.gov.co/~oparra/serv_57/externas/datospatente.php')
fhan = urllib.request.urlopen('http://serviciospub.sic.gov.co/~oparra/serv_57/externas/DetallePatente.php?consultando=patentescolombianas&parametros=opparametros&vano=90&vtra=2&vnum=328450&vcon=%20%20&vcons=0&vcre=35392&vtem=QP')
#pag = open("paginaSIC.txt","w")

for line in fhan:
    texto = str(line.rstrip())
    pag.write(texto[2:-1])
    pag.write('\n')


##Python 4 informatics
#fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
#pag = open("romeo.txt","w")
#
#for line in fhand:
#    #linea = str(line.strip())
#    pag.write(line)
#    #pag.write("\n")


####################################
###### Python 2  ###################
####################################

#import urllib
#
#
########SIC
##fhand = urllib.request.urlopen('http://serviciospub.sic.gov.co/~oparra/serv_57/externas/datospatente.php')
#
########Python 4 informatics
#counts = dict()
#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#
#for line in fhand:
#    words = line.split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
#        print word
#        print counts.get(word, 0)
#        print counts
#
#
#print counts
    
#import urllib
#import re
#url = "http://www.py4inf.com/book.htm" #raw_input('Enter - ')
#html = urllib.urlopen(url).read()
#links = re.findall('href="(http://.*?)"', html)
#for link in links:
#    print link
