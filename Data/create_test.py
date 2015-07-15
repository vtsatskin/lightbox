import json

def create_minutely(time):
	minutely = [{"key": time + 60*x, "values": 20 + (x%6)*(-1)**x} for x in range(60)]
	return minutely

def create_hourly(time):
	hourly = [{"key": time + 3600*x, "values": 15 + (x%6)*(-1)**x} for x in range(24)]
	return hourly

##Dump to text file
hour = create_minutely(1436920200)
hour_json = json.dumps(hour,separators=(',', ': '), sort_keys=True, indent=4)
print (hour[1]['values'])

text_file = open("hour.txt", 'w')
text_file.write(hour_json)
text_file.flush()
text_file.close()

day = create_hourly(1436920200)
day_json = json.dumps(day,separators=(',', ': '), sort_keys=True, indent=4)

text_file = open("day.txt", 'w')
text_file.write(hour_json)
text_file.flush()
text_file.close()

##Test importing
text_file = open("hour.txt", 'r')
hour2 = json.loads(text_file.read())
if hour2 == hour:
	print ("Worked!")
	print (hour2[1]['values'])

