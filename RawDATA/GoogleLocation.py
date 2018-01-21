import csv, time, datetime, json, requests, sys, random, time, base64
GOOGLE_API = base64.b64decode(b'QUl6YVN5Ql9nTU01S1F3ZWFmUWJ6bDByck1KUXdJYnVZTHVSdjg0').decode()
TOWN = "Saint-Hyacinthe"
PRICE_MIN = 7
PRICE_MAX = 60
MAX_KIDS = 6
SLEEP_TIME = 0.1

def Search(item, long = 45.630692, lat = -72.956329, radius = 20000, key = GOOGLE_API):
	URL = """https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="""
	URL += str(long) + ',' + str(lat)
	URL += "&radius=" + str(radius)
	URL += "&keyword=" + item
	URL += "&key=" + key
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	return (data, URL)

def next_page_token(data, URL):
	token = data["next_page_token"]
	url = URL + "&next_page_token=" + token
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	return (data, URL)

def getPlacesID(data, places):
	for element in data["results"]:
		places.add(element["place_id"])
	return places

def getPlaceInfo(placeid, key = GOOGLE_API):
	URL = "https://maps.googleapis.com/maps/api/place/details/json?placeid="
	URL += placeid
	URL += "&key=" + GOOGLE_API
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	data = data["result"]
	place = {}

	place["address"] = data["formatted_address"]
	place["location"] = data["geometry"]["location"]
	place["name"] = data["name"]
	if("rating" in data):
		place["rating"] = data["rating"]
	if("international_phone_number" in data):
		place["tel"] = data["international_phone_number"]
	if("photos" in data):
		place["photos"] = getPhoto(data["photos"][0]["photo_reference"])
	return place


def LookForItem(item):
	placesID = set()
	data, URL = Search(item)
	placesID = getPlacesID(data, placesID)
	while("next_page_token" in data):
		size = len(placesID)
		data, URL = next_page_token(data, URL)
		placesID = getPlacesID(data, placesID)
		if len(placesID) == size:
			break
	return placesID

def getPhoto(reference, key = GOOGLE_API, maxwidth = 400):
	URL = "https://maps.googleapis.com/maps/api/place/photo?maxwidth="+str(maxwidth)+"&photoreference=" + reference
	URL += "&key=" + GOOGLE_API
	time.sleep(SLEEP_TIME)
	return requests.get(url=URL, allow_redirects=True).url

def fakedata(item):
	item["price"] = int(random.randrange(PRICE_MIN, PRICE_MAX) * 100 + 0.5)/100
	item["private"] = bool(random.getrandbits(1))
	item["available"] = int(random.randrange(MAX_KIDS))
	return item

def generateJSON(words):
	items = []
	for item in words:
		items += LookForItem(item)
	js = []
	for i in items:
		p = getPlaceInfo(i)
		p = fakedata(p)
		js.append(p)
	return js

item = ["garderie", "daycare", "childcare"]
with open('DayCare.json', 'w') as outfile:
    json.dump(generateJSON(item), outfile)