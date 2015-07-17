import urllib2
import requests, json, logging

'''
Zipline is our class that handles HTTP requests between CouchDB and any other interface
Creating a new zipline is super simple. Z = Zipline()

//SWITCHING TO COUCHDB PYTHON 
'''

class Zipline(object):
  
  #Initialize a box model with server credentials + user input
  #Should user_id, password be hardcoded if we are just using Val's server
  #def __init__(self, url, user_id, password):
  def __init__(self, url, user_id, password):
    '''
    ##Server authentication credentials
    self.url = url
    self.user_id = user_id
    self.password = password
    self.unique_id = 0
    '''

    #http://valspy.net:5984/model/a7f2669c52fc7e65d229be8a6e005017/

    self.url = url
    self.user_id = user_id
    self.password = password

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
  
  #ARGS -> if our URLs in CouchDB are going to be /box/<id>/args[0]/args[1] etc
  def update_couch_cmd(self, method, *args, **kwargs):
    cmdUrl = "{url}/box/{args}".format(
          url = self.url, 
          args=("/" + "/".join([str(arg) for arg in args]) if args else ""))
    request = self.request(method, cmdUrl, **kwargs)

    return request.json()



