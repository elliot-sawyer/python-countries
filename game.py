import json

country = {}
capital = {}

def getJSON():
	json_string = open("countries.json").read()
	data = json.loads(json_string)
	return data

def makeCapitalsToCountries():
	json = getJSON()
	for i in json['countries']['country']:
		country[i['capital']] = i['countryName'];

def makeCountriesToCapitals():
	json = getJSON();
	for i in json['countries']['country']:
		capital[i['countryName']] = i['capital'];

def getCapitalFrom(countryName):
	print "What is the capital of " + countryName + "?"
	print capital.get(countryName)
def getCountryFrom(capitalCity):
	print capitalCity + " is the capital of which country?"
	print country.get(capitalCity)

makeCapitalsToCountries()
makeCountriesToCapitals()


for capitalCity in country:
	getCountryFrom(capitalCity)

for countryName in capital:
	getCapitalFrom(countryName)
