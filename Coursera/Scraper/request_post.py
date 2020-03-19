import requests
from bs4 import BeautifulSoup

vano = "14"
vnum = "279296"
session = requests.Session()
# url = 'http://serviciospub.sic.gov.co/Sic2/Tramites/Radicacion/Radicacion/Consultas/ConsultaRadicacion.php'
url = "http://serviciospub.sic.gov.co/Sic2/Tramites/Radicacion/Radicacion/Consultas/ConsultaRadicacion.php?vano=" + vano + "&vnum=" + vnum + "&consultando=radi&vcon=&enviar=Consultar"

# payload = {"vano": '15', "fnumeradi":'125621'}
r = requests.get(url)#, params= payload)
#r = session.post(url, data=payload, allow_redirects=True)
#print(r.url)
#print(r.content)
soup = BeautifulSoup(r.content)
# pag = open("paginaSIC.html","w")
# pag.write(soup.prettify())
# print(soup.prettify())

res_table = soup.find("table", id = "tablaResultados")

for item in res_table.find_all("td", style = True):
    # print (item.string.decode("unicode"))
    print (str(item.string), len(str(item.string)))
    
def has_attribute(tag):
    return tag.has_attr("style") or tag.has_attr("colspan") or tag.has_attr("width")