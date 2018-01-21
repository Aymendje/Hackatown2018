import random, csv, time, datetime, json, requests, sys, random, time, base64
DayCare = json.load(open('DayCare.json'))
GOOGLE_API = ""

newJSON = []
for e in DayCare:
	here = False
	for i in newJSON:
		if(i["address"] == e["address"]):
			here = True
			break
	if not here:
		newJSON.append(e)
	

with open('DayCareClean.json', 'w') as outfile:
    json.dump(newJSON, outfile)