import numpy as np
import pandas as pd
from sklearn import  linear_model

import json


##Test Regresion##
x = np.array([[x,0] for x in range(20)])
y = np.array([[y*2] for y in range(20)])
print(len(x))
print(len(y))
#regr = linear_model.LinearRegression()
#regr.fit(x,y)
#print (regr.coef_)
#print(regr.intercept_)

##Data Conversion
text_file = open("../data/hour.txt", 'r')
minutely = json.loads(text_file.read())

def average_hour(minutely):
	total = 0
	time = 0
	for minute in minutely:
		total = total + minute['value']
		time = time + minute['key']
	timestamp = int(time/(len(minutely)))
	average = total/(len(minutely))
	hour = { "key" : timestamp, "value" : average}
	return hour

hour = average_hour(minutely)

text_file = open("../data/day.txt", 'r')
day = json.loads(text_file.read())

def find_equal(hour, day):
	for h in day:
		if h["key"] == hour["key"]:
			return h

eql = find_equal(hour,day)

def difference(reading1, reading2, check = True):
	if(not check or reading2["key"]==reading1["key"]):
		return (reading2["value"]-reading1["value"])

##def grab_hour(min_day, ts):


##def create_comparable(min_day,hour_day):
	##for h in hour_day:
		##hour = grab_hour(min_day, h["value"])

print(difference(eql, hour))

