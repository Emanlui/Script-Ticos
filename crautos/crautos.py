import requests, re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
		"Cookie":"_ga_VSKP37KZJC=GS1.1.1638756062.1.1.1638757601.0; _ga=GA1.2.866334335.1638756063; __asc=a4bf2cf617d8d7918a9c21a9d9f; __auc=a4bf2cf617d8d7918a9c21a9d9f; _gid=GA1.2.1947919661.1638756064; _fbp=fb.1.1638756067181.1017125405; __gads=ID=0031512d8cd5a06d-225998cb84ce008c:T=1638756068:S=ALNI_MbmMSUSli4VhzNpXcqqjg_AEMPb8w; _gat_gtag_UA_2824303_1=1",
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language":"en-US,en;q=0.5",
	"Accept-Encoding":"gzip, deflate",
	"Content-Type":"application/x-www-form-urlencoded",
	"Content-Length":"176",
	"Origin":"https://crautos.com",
	"Referer":"https://crautos.com/autosusados/",
	"Upgrade-Insecure-Requests":"1",
	"Te":"trailers"
		
	}


# Parametro opcional en caso de querer debuggear los request, se pone en el .post 
# 																proxies=proxies
proxies = {
	"http": "http://127.0.0.1:8080",
	"https": "http://127.0.0.1:8080",
}

file = open("carros.txt", "w")
for num in range(1,100):

	# Esto se debe de cambiar, es el search que uno quiere hacer, se encuentra cuando uno hace una búsqueda
	data = "brand=00&financed=00&yearfrom=1960&yearto=2022&pricefrom=3000000&priceto=5000000&style=00&province=0&doors=0&orderby=0&newused=1&fuel=0&trans=0&recibe=0&modelstr=&totalads=1482&p=" + str(num)
	r = requests.post("https://crautos.com/autosusados/searchresults.cfm?="+str(12050 + num), headers=headers,data=data,verify=False)
	carros = re.findall("cardetail\.cfm\?c.*\">",r.text)
	for cont,i in enumerate(carros):

		headers_carro = {
		"Cookie":"_ga_VSKP37KZJC=GS1.1.1638756062.1.1.1638758088.0; _ga=GA1.2.866334335.1638756063; __asc=a4bf2cf617d8d7918a9c21a9d9f; __auc=a4bf2cf617d8d7918a9c21a9d9f; _gid=GA1.2.1947919661.1638756064; _fbp=fb.1.1638756067181.1017125405; __gads=ID=0031512d8cd5a06d-225998cb84ce008c:T=1638756068:S=ALNI_MbmMSUSli4VhzNpXcqqjg_AEMPb8w",
		"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language":"en-US,en;q=0.5",
		"Accept-Encoding":"gzip, deflate",
		"Referer":"https://crautos.com/autosusados/showcarpic.cfm?c=46024237&p=46024237-t.jpg",
		"Upgrade-Insecure-Requests":"1",
		"Te":"trailers",
		}
		
		carros = requests.get("https://crautos.com/autosusados/"+i[:-2], headers=headers_carro,verify=False)
		
		kilometraje = re.findall(".*km",carros.text)
		titulo = re.findall("<title>crautos.com - Autos Usados Costa Rica.*</title>",carros.text)

		# Este filtro de fechas se debe de cambiar, esto es en caso de que se quiera filtrar por fecha
		# Ya que la pagina no lo permite...
		fecha_de_ingreso = re.findall("(15|16|17|18|19|20) de Enero del 2022</td>",carros.text)
		
		precio = re.findall("<h2>&cent;.*</h2>",carros.text)
		if fecha_de_ingreso:
			try:	
				if kilometraje:
					kilometraje = str(kilometraje).split("\\t")[1][:-5].replace(",","")
					
					# Depende de los kilometrajes que se quieran buscar
					if(int(kilometraje) <= 110000):
						
						print(f"{precio[0][12:-5]} Colones")
						file.write("--------")
						file.write("\n")
						file.write("https://crautos.com/autosusados/"+i[:-2])
						file.write("\n")
						file.write(str(titulo).split(".")[2][1:-10])
						file.write("\n")
						file.write(f"{kilometraje} km")
						file.write("\n")
						file.write(f"{fecha_de_ingreso} de Diciembre")
						file.write("\n")
						file.write(f"{precio[0][12:-5]} Colones")
						file.write("\n")
						
			except Exception:
				pass	
		if(cont == 15):
			break

file.close()
