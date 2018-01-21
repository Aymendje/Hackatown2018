import csv, time, datetime, json, requests, sys, random, time, base64
GOOGLE_API = base64.b64decode(b'QUl6YVN5Ql9nTU01S1F3ZWFmUWJ6bDByck1KUXdJYnVZTHVSdjg0').decode()
TOWN = "Saint-Hyacinthe"
PRICE_MIN = 200
PRICE_MAX = 2000
MAX_KIDS = 25
SLEEP_TIME = 0.1

GLOBAL_CALLS = 0

def Search(item, long = 45.630692, lat = -72.956329, radius = 20000, key = GOOGLE_API):
	global GLOBAL_CALLS
	URL = """https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="""
	URL += str(long) + ',' + str(lat)
	URL += "&radius=" + str(radius)
	URL += "&keyword=" + item
	URL += "&key=" + key
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	GLOBAL_CALLS += 1
	return (data, URL)

def next_page_token(data, URL):
	global GLOBAL_CALLS
	token = data["next_page_token"]
	url = URL + "&next_page_token=" + token
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	GLOBAL_CALLS += 1
	return (data, URL)

def getPlacesID(data, places):
	global GLOBAL_CALLS
	for element in data["results"]:
		places.add(element["place_id"])
	return places

def getPlaceInfo(placeid, key = GOOGLE_API):
	global GLOBAL_CALLS
	URL = "https://maps.googleapis.com/maps/api/place/details/json?placeid="
	URL += placeid
	URL += "&key=" + GOOGLE_API
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	GLOBAL_CALLS += 1
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
	global GLOBAL_CALLS
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
	global GLOBAL_CALLS
	URL = "https://maps.googleapis.com/maps/api/place/photo?maxwidth="+str(maxwidth)+"&photoreference=" + reference
	URL += "&key=" + GOOGLE_API
	time.sleep(SLEEP_TIME)
	GLOBAL_CALLS += 1
	return requests.get(url=URL, allow_redirects=True).url

def fakedataPlace(item):
	global GLOBAL_CALLS
	item["price"] = int(random.randrange(PRICE_MIN, PRICE_MAX) * 100 + 0.5)/100
	item["private"] = bool(random.getrandbits(1))
	item["available"] = int(random.randrange(MAX_KIDS))
	return item

def generateJSONPlace(words):
	global GLOBAL_CALLS
	items = []
	for item in words:
		items += LookForItem(item)
	js = []
	for i in items:
		p = getPlaceInfo(i)
		p = fakedataPlace(p)
		js.append(p)
	return js



def getPlaceInfo(placeid, key = GOOGLE_API):
	global GLOBAL_CALLS
	URL = "https://maps.googleapis.com/maps/api/place/details/json?placeid="
	URL += placeid
	URL += "&key=" + GOOGLE_API
	time.sleep(SLEEP_TIME)
	data = json.loads(requests.get(url=URL).text)
	data = data["result"]
	GLOBAL_CALLS += 1
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

def fakedataSports(item, sport):
	global GLOBAL_CALLS
	item["price"] = int(random.randrange(PRICE_MIN, PRICE_MAX) * 100 + 0.5)/100
	item["private"] = bool(random.getrandbits(1))
	item["available"] = int(random.randrange(MAX_KIDS))
	item["sport"] = sport
	return item

def generateJSONSports(words):
	global GLOBAL_CALLS
	items = []
	js = []
	for item in words:
		print(GLOBAL_CALLS)
		items += LookForItem(item)
	for i in items:
		print(GLOBAL_CALLS)
		p = getPlaceInfo(i)
		p = fakedataSports(p, words)
		js.append(p)
	return js

"""
item = ["garderie", "daycare", "childcare"]
with open('DayCare.json', 'w') as outfile:
    json.dump(generateJSONPlace(item), outfile)
"""
item = []
items = ["archery", "badminton", "baseball", "softball", "basketball", "beach volleyball", "boxing", "canoe", "kayak", "climbing", "cycling ", "diving", "equestrian", "fencing", "field hockey", "golf", "gymnastics", "handball", "judo", "karate", "pentathlon", "roller sport", "rowing", "sailing", "shooting", "soccer", "football", "swimming", "surfing", "table tennis", "taekwondo", "tennis", "track and field", "triathlon", "volleyball", "water polo", "weightlifting", "wrestling", "baseball ", "rugby", "squash", "wakeboard", "wushu", "dancing", "bowling", "netball", "Boxing", "Pankration", "Running", "Wrestling"]
for it in [[i] for i in items]:
	item += generateJSONSports(it)


sortedlist = []
for item in item:
    if item not in sortedlist:
        sortedlist.append(item)

with open('Sports.json', 'w') as outfile:
    json.dump(sortedlist, outfile,  indent=4)