import random, csv, time, datetime, json, requests, sys, random, time, base64
postalCode = json.load(open('PostalCode.json'))
GOOGLE_API = ""

def Search(item, key = GOOGLE_API):
	URL = "https://maps.googleapis.com/maps/api/geocode/json?address="+item+"+QC"
	URL += "&key="+GOOGLE_API
	time.sleep(0.1)
	data = json.loads(requests.get(url=URL).text)
	if(len(data["results"]) == 0):
		time.sleep(2)
		data = json.loads(requests.get(url=URL).text)
		if(len(data["results"]) == 0):
			data["results"] = [{"geometry" : { "location" : { "lng" : None, "lat" : None}}}]
	data = data["results"][0]["geometry"]["location"]
	return (data)

newJSON = []
for i in range(len(postalCode)):
	e = postalCode[i]
	o = {}
	o["postal"] = list(e.keys())[0]
	o["address"] = e[o["postal"]]
	o["location"] = Search(o["postal"])
	newJSON.append(o)
	print(i * 1.0 / len(postalCode) * 100)

with open('test.json', 'w') as outfile:
    json.dump(newJSON, outfile)