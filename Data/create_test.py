import json
import numpy as np

def create_minutely(time, hours):
	minutely = [{"key": time + 60*x, "value": np.random.normal(25, 1) + (x/60)%300} for x in range(60*hours)]
	return minutely

def create_hourly(time):
	hourly = [{"key": time + 3600*x, "value": np.random.normal(20, 1) + x%5} for x in range(24)]
	return hourly

##Dump to text file
hour = create_minutely(1436920200 - 1770, 1)
hour_json = json.dumps(hour,separators=(',', ': '), sort_keys=True, indent=4)
print (hour[1]['value'])

text_file = open("hour.txt", 'w')
text_file.write(hour_json)
text_file.flush()
text_file.close()

min_day = create_minutely(1436920200 - 1770, 24)
min_day_json = json.dumps(min_day,separators=(',', ': '), sort_keys=True, indent=4)


text_file = open("min_day.txt", 'w')
text_file.write(min_day_json)
text_file.flush()
text_file.close()

day = create_hourly(1436920200)
day_json = json.dumps(day,separators=(',', ': '), sort_keys=True, indent=4)

text_file = open("day.txt", 'w')
text_file.write(day_json)
text_file.flush()
text_file.close()

##Test importing
text_file = open("hour.txt", 'r')
hour2 = json.loads(text_file.read())
if hour2 == hour:
	print ("Worked!")
	print (hour2[1]['value'])

