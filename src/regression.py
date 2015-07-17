import numpy as np
import pandas as pd
from sklearn import  linear_model

import json

##Loading test files
text_file = open("../data/hour.txt", 'r')
minutely = json.loads(text_file.read())

text_file = open("../data/day.txt", 'r')
day = json.loads(text_file.read())

text_file = open("../data/min_day.txt", 'r')
min_day = json.loads(text_file.read())

########################
##Function definitions##
########################

def average_hour(minutely, value="value", key="key"):
	"""
		Takes minutely data for an hour.
		Returns a Json object containing the average 
		timestamp and value.

		To do: Make averaging of timestamp optional.
	"""
	total = 0
	time = 0
	for minute in minutely:
		total = total + minute[value]
		time = time + minute[key]
	if len(minutely) > 0:
		timestamp = int(time/(len(minutely)))
		average = total/(len(minutely))
	hour = { key: timestamp, value : average}
	return hour

##Not Currently using this
def find_equal(hour, day):
	for h in day:
		if h["key"] == hour["key"]:
			return h

##Not currently using this
def difference(reading1, reading2, check = True, value="value", key="key"):
	if(not check or reading2[key]==reading1[key]):
		return (reading2[value]-reading1[value])

def grab_hour(min_day, ts, key="key"):
	"""
		Takes a minutely data set for a given time period and a unix timestamp. 
		Returns the minutely data for the hour centered about the timestamp
		in a json list of the same format.
	"""
	hour = []
	for min in min_day:
		if min[key] > ts - 1830 and min[key] < ts + 1830:
			hour.append(min)
	return hour		

def regress_different(min_day,hour_day, value="value", key="key"):
	"""
		Takes a minutely data set and an hourly data set and preforms
		a Linear Regression on the data sets. It returns a LinearRegression
		object from the linear_model module. 
	"""
	x = []
	y = []
	for h in hour_day:
		hour = grab_hour(min_day, h[key])
		hour = average_hour(hour)
		#print(h)
		#print(hour)
		x.append([h[value],0])
		y.append(hour[value])
	#print(x)
	#print(y)
	regr = linear_model.LinearRegression()
	regr.fit(x,y)
	return regr

##Testing Regression
regr = regress_different(min_day, day)
print (regr.coef_)
print (regr.intercept_)