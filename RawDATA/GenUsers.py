filename = "FakeNameGenerator.com_049d5686.csv"
myFile = open(filename, encoding="utf-8").readlines()
HEADER = ["Number", "Gender", "NameSet", "Title", "GivenName", "MiddleInitial", 
"Surname", "StreetAddress", "City", "State", "StateFull", "ZipCode", "Country", 
"CountryFull", "EmailAddress", "Username", "Password", "BrowserUserAgent", 
"TelephoneNumber", "TelephoneCountryCode", "MothersMaiden", "Birthday", "Age", 
"TropicalZodiac", "CCType", "CCNumber", "CVV2", "CCExpires", "NationalID", "UPS", 
"WesternUnionMTCN", "MoneyGramMTCN", "Color", "Occupation", "Company", "Vehicle", 
"Domain", "BloodType", "Pounds", "Kilograms", "FeetInches", "Centimeters", "GUID", 
"Latitude", "Longitude"]

myFile = myFile[1:]
for i in range(len(myFile)):
	myFile[i] = myFile[i].replace('"','').split(',')
print(myFile[-1])
