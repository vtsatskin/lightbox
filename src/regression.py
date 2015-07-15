import numpy as np
import pandas as pd
from sklearn import  linear_model

import json

##Test Regresion##
x = np.array([[x,0] for x in range(20)])
y = np.array([[y*2] for y in range(20)])
print(len(x))
print(len(y))
regr = linear_model.LinearRegression()
regr.fit(x,y)
print (regr.coef_)
print(regr.intercept_)

##Data Conversion
text_file = open("../data/hour.txt", 'r')
minutely = json.loads(text_file.read())
total = 0
for minute in minutely:
	total = total + minute['values']
average = total/(len(minutely))
print(average)
