import random, csv, time, datetime, json, requests, sys, random, time, base64
GOOGLE_API = base64.b64decode(b'QUl6YVN5Ql9nTU01S1F3ZWFmUWJ6bDByck1KUXdJYnVZTHVSdjg0').decode()
filename = "FakeNameGenerator.com_049d5686.csv"
myFile = open(filename).readlines()
postalCode = json.load(open('PostalCode.json'))
myFile = [i for i in myFile[1:]]
people = []
p = 0
p2 = 0
for i in range(len(myFile)):
	myFile[i] = myFile[i].split('\t')
	obj = {}
	obj["id"] = int(myFile[i][0])
	if(myFile[i][1] == "male"):
		obj["gender"] = True
	else:
		obj["gender"] = False
	obj["givenName"] = myFile[i][2]
	obj["surName"] = myFile[i][3]
	obj["zipCode"] = postalCode[p]["postal"]
	obj["streetAddress"] = postalCode[p]["address"][p2]
	obj["emailAddress"] = myFile[i][6]
	obj["userName"] = myFile[i][7]
	obj["password"] = myFile[i][8]
	obj["telephoneNumber"] = myFile[i][9]
	obj["birthday"] = myFile[i][10]
	obj["age"] = int(myFile[i][11])
	obj["creditCardType"] = myFile[i][12]
	obj["creditCardNumber"] = int(myFile[i][13])
	obj["CVV2"] = int(myFile[i][14])
	obj["creditCardExpirationDate"] = myFile[i][15]
	obj["SSN"] = int(myFile[i][16].replace(' ', ''))
	obj["occupation"] = myFile[i][17]
	obj["company"] = myFile[i][18]
	obj["vehicle"] = myFile[i][19]
	obj["bloodType"] = myFile[i][20]
	obj["mass"] = float(myFile[i][21])
	obj["height"] = int(myFile[i][22])
	obj["location"] = postalCode[p]["location"]

	people.append(obj)
	if(p2 == len(postalCode[p]["address"]) - 1):
		p += 1
		p2 = 0
	else:
		p2 += 1
	if(p >= len(postalCode)):
		p = 0

with open('People.json', 'w') as outfile:
    json.dump(people, outfile, indent=4)

