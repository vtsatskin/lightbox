import csv, os

def csv2json(csv_name):
	with open(csv_name) as csv_file:
		reader = csv.DictReader(csv_file)
		names = reader.fieldnames
		print names

##path = input("File Path: ")
##os.chdir(path)
test = input("File Name: ")
csv2json(test)
