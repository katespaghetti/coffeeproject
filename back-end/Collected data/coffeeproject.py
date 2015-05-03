import sys
import urllib2
import json
import csv

url = "https://openapi.starbucks.com/v1/stores/nearby?callback=&radius=50&limit=50&latLng={0}%2C{1}&access_token=v53hgty3cgfa87tda6k9uxxx"

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

		#06073
		#08989
		#12490
		#20001
		#27359
		#31558
		#38341 
		#43127 between this number and the next, save as 6a
		#47403
		#56309
		#63108
		#64188
		#74960
		#82729
		#85219
		#89116
		#89434
		#90632
		#91103
		#92018
		#92199
		#92604
		#96820

		
		if int(zip_code) <= 43127 or int(zip_code) >= 47403:
			continue
		
		if lat == "0" or lng == "0":
			continue

		print zip_code, lat, lng
		print url.format(lat,lng)

		response = urllib2.urlopen(url.format(lat,lng))
		data = json.load(response)
		
		for stores in data["stores"]:
			if str(stores["store"]["address"]["postalCode"]).startswith(zip_code):
				starbucks_stores.append(stores["store"])
				f = open('range.json', 'w')
				json.dump(starbucks_stores, f)
				f.close()
				print "Kisses!"

		#break

#f.close()


