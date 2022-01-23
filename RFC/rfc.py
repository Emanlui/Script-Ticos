import requests
import json

url = "https://www.rfc-editor.org/rfc/rfc"

data = ""

for i in range(1000,9137):

	json_url = url + str(i) + ".json"

	r = requests.get(json_url)
	  
	json_data = r.content.decode()
	try:
		json_load_data = json.loads(json_data)
		data += json_load_data['doc_id'] + " - " + json_load_data['title'] + " - " + json_load_data['abstract'] + "\n"
	except:
		print(json_load_data)
		data += json_load_data['doc_id'] + " - " + json_load_data['title'] + "\n"
	print(i)
f = open("rfc.txt", "w")
f.write(data)
f.close()


