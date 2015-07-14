import urllib2

class BoxModel(object):
  
  #dummy data from user input
  def __init__(self, post):
    self.historical = post['historical']
    self.shading_efficiency = 0
    self.avgTempCoefficient = 0
  	self.tempCoefficientList = []
  
              
  #Efficiency Temperature Portion of Model 
  def avg_coefficient(self, histHourly, actualHourly):
  	'''Calculate temperature T = Tamb + Coefficient'''
                           
    actualHourly - histHourly = tempCo
    self.tempCoefficientList.append(abs(tempCoefficient))
    return sum(self.tempCoefficientList)/(float(len(self.tempCoefficientList)))
  
  def avg_hist_temp(self, hist):
    return sum(hist)/len(hist)
  
  def temperature_efficiency(self, avgCoefficient, avgHistTemp):
    return avgCoefficient + avgHistTemp
    
  #Efficiency Shading
	def shading_efficiency(self, percentA, percentLight):
		self.shading_efficiency = percentA*percentLight                           
  #Efficiency degradation
	def panel_degradation_efficiency(self, year):
    return 0.99**year
                      
#HTTP CLASS , place import at type of file
import requests
    ''' 
    Example requests
  	--------------------------------------------
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.get("http://httpbin.org/get", params=payload)
    
    Response 
    --------------------------------------------
	r.text
    r.json() 
    
    Custom Headers
    --------------------------------------------
    
    headers = {'user-agent': 'my-app/0.0.1'}
	r = requests.get(url, headers=headers)
  
    '''