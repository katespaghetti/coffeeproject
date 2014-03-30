import json

conc_var = []

data_list = ["output22", "output21", "output20", "output19", "output18", "output17", "output16", "output15", "output14", "output13", "output12", "output11", "output10", "output9", "output8", "output7", "output6", "output5", "output4", "output3", "output2", "output1"]

for each_element in data_list: 
	with open(each_element + ".txt","rw") as one_of_them:
		each_file = json.load(one_of_them)
		print len(each_file)

		conc_var += each_file

print len(conc_var)

f = open('starbucks.json', 'w')
json.dump(conc_var, f)
f.close()
print "Merged!"