import numpy as np
#import pandas as pd
from sklearn import  linear_model

import couchdb

import json


text_file = open("../data/hour.txt", 'r')
minutely = json.loads(text_file.read())

text_file = open("../data/day.txt", 'r')
day = json.loads(text_file.read())

text_file = open("../data/min_day.txt", 'r')
min_day = json.loads(text_file.read())

def average_hour(minutely):
	total = 0
	time = 0
	for minute in minutely:
		total = total + minute['value']
		time = time + minute['key']
	if len(minutely) > 0:
		timestamp = int(time/(len(minutely)))
		average = total/(len(minutely))
	hour = { "key" : timestamp, "value" : average}
	return hour

def find_equal(hour, day):
	for h in day:
		if h["key"] == hour["key"]:
			return h

def difference(reading1, reading2, check = True):
	if(not check or reading2["key"]==reading1["key"]):
		return (reading2["value"]-reading1["value"])

def grab_hour(min_day, ts):
	hour = []
	for min in min_day:
		if min["key"] > ts - 1830 and min["key"] < ts + 1830:
			hour.append(min)
	return hour		

def compare(min_day,hour_day):
	x = []
	y = []
	for h in hour_day:
		hour = grab_hour(min_day, h["key"])
		hour = average_hour(hour)
		#print(h)
		#print(hour)
		x.append([h["value"],0])
		y.append(hour["value"])
	#print(x)
	#print(y)
	regr = linear_model.LinearRegression()
	regr.fit(x,y)
	return regr


couch = couchdb.Server()
couch.resource.credentials = ()
modelDb = couch['model']


regr = compare(min_day, day)
print regr.coef_
print regr.intercept_

updatedData = regr.coef_.tolist()
print type(updatedData[0])

json = json.dumps(updatedData[0])

print json
print type(json)

doc = modelDb['test']
doc['temperatureCoefficient'] = json
modelDb.save(doc) 


