import json
import csv

coordinates = []
coordinate_file = "Polygons_Working_File_2010.csv"

with open("coordinate_file.csv", "rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"') 



#if each_coordinate != float:
#	continue

#for each_coordinate in coordinate_file:
#	coordinates.reverse[::-1]


#response = new google.maps.LatLng([-71.8986952356,42.7114663615])