#Encontrar datos en las paginas con RE
import re
from bs4 import BeautifulSoup
import codecs

CAMPOS = ('Expediente', 'Fecha de solicitud', 'Sector', 'Clasificaci\xf3n Ipc', 'Clasificación Ipc',
          'T\xedtulo', 'Título', 'Solicitante(s)', 'Estado', 'Inventor(es)', 'Resumen', 'Apoderado',
          'Actos Administrativos')
##################
#####EJERCICIO####
#hand = open("romeo.txt")
#for line in hand:
#    line = line.strip().lower()
#    #print (type(line))
#    print(re.search("but", line))
#    if re.search("but", line):
#        print (line)

##################################
#############SIC#################

hand = open("paginaSIC3.html")
soup = BeautifulSoup(hand)
pag = open('ensayo_borrar.txt', 'w')

#### Pruebas de soup para imprimir bonito
#print(soup.get_text())
print(soup.prettify())
######print (tag.name)
### Función para devolver los tag con atributo colspan = "2"
#def has_att(attri):
#    return attri == "2"
#               10

#campo_imp = '0'
#flag = False
#for each_tag in soup.find_all("td"):
#    str_tag = str(each_tag)
#    striped_tag = re.findall('>(.+)</td', str_tag)
#    if len(striped_tag) > 0 and type(striped_tag) == list:
#        striped_tag = striped_tag[0]
#    if type(striped_tag) == str:
#        coded_tag = striped_tag.encode('utf8')
#        decode_tag = coded_tag.decode('utf8')
#        for campo in CAMPOS:
#            if campo == decode_tag:
#                flag = True
#                campo_imp = campo
#                pag.write(campo_imp + ": ")
#                break
#        
#        if flag and campo_imp != decode_tag:
#            print ('imp', campo_imp, 'tag', decode_tag, 'flag', flag)
#            pag.write(decode_tag)
#            pag.write("\n")
#            flag = False
        #print( decode_tag)


#### RE: Regular Expression
#for line in hand:
#    texto = str(line.rstrip())
#    print (re.search('<td.> [0-9A-Za-z\/] </td>', texto))

#print(soup.td)
#texto = '<td colspan="2" class="title" width="12%">Fecha de solicitud</td>'
#extraido = re.findall('>(.+)</td', texto)
#print (extraido[0])
