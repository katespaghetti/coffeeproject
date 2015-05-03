import json
import csv

coordinates = []
coordinate_file = "Polygons_Working_File_2010_v2.csv"

with open(coordinate_file, "rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')

	# Loop through each line (county) in the file
	
	for countyRow in reader:
		eachRowCoordinates = []
		
		for rowElement in countyRow:
			try:
				improvedRowElement = float(rowElement.replace("0 ", "")) # "0 " was between data points instead of "" in original csv 
				if type(improvedRowElement) == float:
					eachRowCoordinates.append(improvedRowElement)
			except ValueError:
				coordinates.append(eachRowCoordinates[::-1])
				break
		
f = open("coordinates.json","w")
json.dump(coordinates, f)
f.close()



#if each_coordinate != float:
#	continue

#for each_coordinate in coordinate_file:
#	

#response = new google.maps.LatLng([-71.8986952356,42.7114663615])