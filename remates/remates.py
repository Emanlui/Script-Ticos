import requests, re
import PyPDF2
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from datetime import datetime, timedelta

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getData(primero,segundo,limite_1,limite_2,data):
	temp_primero = data.find(limite_1,segundo)
	temp_segundo = data.find(limite_2,temp_primero)

	if(temp_primero == -1 or temp_segundo == -1):
		return primero,segundo,"-"
	else:
		informacion = data[temp_primero:temp_segundo]
		return temp_primero,temp_segundo,informacion


def filtrarVehiculo(data):

	primero = data.find("base de")
	segundo = data.find(",",primero)
	print(data[primero:segundo])
	
	primero,segundo,informacion = getData(primero,segundo,"vehículo",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"marca",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"estilo",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"categoría",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"capacidad",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"tracción",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"año",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"color",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"cilindrada",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"VIN",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"base de","(",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"base de","(",data)
	print(informacion)
	
	print("-----")

def filtrarTerreno(data):

	primero = data.find("base de")
	segundo = data.find(",",primero)
	print(data[primero:segundo])

	primero,segundo,informacion = getData(primero,segundo,"partido",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"matrícula",",",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"ituada",".",data)
	print("S" + informacion)

	primero,segundo,informacion = getData(primero,segundo,"Mide",".",data)
	print(informacion)
	
	primero,segundo,informacion = getData(primero,segundo,"base de","(",data)
	print(informacion)

	primero,segundo,informacion = getData(primero,segundo,"base de","(",data)
	print(informacion)

	print("-----")
	
def boletin():

	x = datetime.now() - timedelta(days=10)
	url = 'https://www.imprentanacional.go.cr/boletin/?date=07/01/2022'
	r = requests.get(url, allow_redirects=True,verify=False)

	

	primero = r.text.find("SEGUNDA PUBLICACIÓN")
	segundo = r.text.find("Citaciones")

	codigo = r.text[primero:segundo].rstrip().replace("\n","").replace("\r","")

	
	p = re.compile(r'<.*?>')
	tmp = p.sub('', codigo)
	lista_de_remates = tmp.split("despacho")

	for i in lista_de_remates:

		# Vehiculo
		if("vehículo" in i):
			filtrarVehiculo(i)
		# Terreno 
		if("terreno" in i):
			#filtrarTerreno(i)
			print()

def gaceta():

	x = datetime.now() - timedelta(days=7)
	url = 'https://www.imprentanacional.go.cr/Gaceta/?date=10/01/2022'
	r = requests.get(url, allow_redirects=True,verify=False)

	primero = r.text.find("AVISOS")
	segundo = r.text.find("INSTITUCIONES DESCENTRALIZADAS")

	codigo = r.text[primero:segundo].rstrip().replace("\n","").replace("\r","")

	
	p = re.compile(r'<.*?>')
	tmp = p.sub('', codigo)
	lista_de_remates = tmp.split("despacho")

	for i in lista_de_remates:

		# Vehiculo
		if("vehículo" in i):
			filtrarVehiculo(i)
		# Terreno 
		if("terreno" in i):
			#filtrarTerreno(i)
			print()

#boletin()
gaceta()