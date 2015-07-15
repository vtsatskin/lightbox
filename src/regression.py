import numpy as np
from sklearn import  linear_model

x = np.array([[x,0] for x in range(20)])
y = np.array([[y*2] for y in range(20)])
print(len(x))
print(len(y))
regr = linear_model.LinearRegression()
regr.fit(x,y)
print (regr.coef_)
print(regr.intercept_)

