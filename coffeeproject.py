import sys
import urllib2
import json
import csv

#https://openapi.starbucks.com/v1/stores/nearby?callback=&radius=50&limit=50&latLng=42.3716445%2C-71.08097570000001&access_token=779surgjsvaehjmnjyj2hbfa

#https://openapi.starbucks.com/v1/stores/nearby?callback=jQuery17209275648959446698_1393991545347&radius=50&limit=50&latLng=42.3716445%2C-71.08097570000001&ignore=storeNumber%2CownershipTypeCode%2CtimeZoneInfo%2CextendedHours%2ChoursNext7Days&brandCodes=SBUX&access_token=afkbs6c3md2dcdesqk64tt3s&_=1393991697540

url = "https://openapi.starbucks.com/v1/stores/nearby?callback=&radius=50&limit=50&latLng={0}%2C{1}&access_token=779surgjsvaehjmnjyj2hbfa"
url2 = "https://openapi.starbucks.com/v1/stores/nearby?callback=&radius=50&limit=50&latLng={0}%2C{1}&access_token=bxda6upxkn25f9gtsctqeda3"

starbucks_stores = []
zip_filename = "zip_code_database.csv"
#f = open(zip_filename)
#for line in f:

with open(zip_filename, 'rb') as csvfile: 
    reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
    for line in reader:

    	#"02141"
 		#42.37164
 		#-71.08098

		zip_code = line[0].strip('"')
		lat = line[9].strip('"')
		lng = line[10].strip('"')

		print zip_code, lat, lng
		print url2.format(lat,lng)

		response = urllib2.urlopen(url2.format(lat,lng))
		data = json.load(response)   
		#print data["stores"]
		
		for stores in data["stores"]:
			if str(stores["store"]["address"]["postalCode"]).startswith(zip_code):
				starbucks_stores.append(stores["store"])
				print "Kisses!"


		#break

#f.close()

print starbucks_stores

f = open('output.txt', 'w')
json.dump(starbucks_stores, f)
f.close()



