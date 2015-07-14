import urllib2
import xml.etree.ElementTree as ET

import datetime.datetime
                           
class LocalTempReading(object)
                           
    def __init__(self,city_code):
        self.temp = 0
        self.city_code = city_code
                           
    def temperature_reading():
        file = urllib2.urlopen('http://dd.meteo.gc.ca/citypage_weather/xml/ON/'+ self.city_code +'_e.xml')
        tree = ET.parse(file)
        root = tree.getroot()
        current_conditions = root.find('currentConditions')
        self.temp = int(current_conditions.find('temperature').text)
        hour = int(current_conditions[2].find('hour').text) 
        minute = int(current_conditions[2].find('minute').text)
        year = int(current_conditions[2].find('year').text)
        month = int(current_conditions[2].find('month').text)
        day = int(current_conditions[2].find('day').text)
        self.dt = datetime(year, month, day, hour, minute)
        file.close()