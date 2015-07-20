import csv
import json

def csv2json(csv_name):
	data = open("historical.json", 'w')
	upload_to_couch = { "docs" : 0}
	dict_list = []
	with open(csv_name) as csv_file:
		reader = csv.DictReader(csv_file)
		names = reader.fieldnames
		for row in reader:
			dict_list.append(row)
	upload_to_couch["docs"]	= dict_list
	upload = json.dumps(upload_to_couch, separators=(',', ': '), sort_keys=True, indent=4)
	data.write(upload)
	data.flush()
	data.close()		

		
	

data = input("File Name: ")
csv2json(data)
