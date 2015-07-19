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

def couch_mapreduce(map_fun, reduce_fun):
	"""Takes all temperature from couchDB
		and returns the hourly average
	"""	

def regression(m_x, r_x, m_y, r_y):
	"""	A Linear Regression on two data sets from couchDB. It returns a LinearRegression
		object from the linear_model module. 
	"""
	x = []
	y = []
	readings_x = couch_mapreduce(m_x, r_x)
	readings_y = couch_mapreduce(m_y, r_y)
	for read_x in readings_x:
		for read_y in hourly_EC:
			if read_x == read_y:
				x.append([readings_x[read_x],0])
				y.append(readings_y[read_y])
	regr = linear_model.LinearRegression()
	regr.fit(x,y)
	return regr


couch = couchdb.Server()
couch.resource.credentials = ()
modelDb = couch['model']


regr = regress_hourly()
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


