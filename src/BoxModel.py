import urllib2
import requests, json, logging

class BoxModel(object):
  
  #Initialize a box model with server credentials + user input
  def __init__(self, post, url, user_id, password):
    """ 
    Should user_id, password be hardcoded if we are just using Val's server
    """

    self.historical = post['historical']
    self.shading_efficiency = 0
    self.avgTempCoefficient = 0
    self.tempCoefficientList = []

    ##Server authentication credentials
    self.url = url
    self.user_id = user_id
    self.password = password
    self.unique_id = 0

  #HTTP Methods
  def request(self, method, url, **kwargs):
    """
    method = http method for request
    url = url/endpoint for request
    kwargs --
    params:url parameters
    data: data to be converted to json
    """
    data = (json.dumps(kwargs['data']) if "data" in kwargs else None)
    headers = ({'content-type':'application/json'} if data else None)
    params = (kwargs['params'] if "params" in kwargs else None)
    request = method(url, auth=(self.user_id, self.password), params = params, data=data, headers=headers)
    request.raise_for_status()
    return request
  
  #def updateCoefficientModel (self, coefficientData):
  #ARGS -> if our URLs in CouchDB are going to be /box/<id>/args[0]/args[1] etc

  def updateBox_cmd(self, method, id, *args, **kwargs):
    cmdUrl = "{url}/box/id/{args}".format(
          url = self.url, 
          args=("/" + "/".join([str(arg) for arg in args]) if args else ""))
    request = self.request(method, cmdUrl, **kwargs)

    return request.json()


  #Efficiency Temperature Portion of Model 
  def avg_coefficient(self, readings):
    '''Calculate temperature T = Tamb + Coefficient'''

    readings['actualHourly'] - readings['histHourly'] = tempCo
    self.tempCoefficientList.append(abs(tempCoefficient))
    avg = sum(self.tempCoefficientList)/(float(len(self.tempCoefficientList)))

    payload = [{'avgCoefficient':avg}]
    self.updateBox_cmd(requests.post, self.unique_id, data=payload)  


  
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
                      
#HTTP CLASS , place import at top of file
#import requests
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