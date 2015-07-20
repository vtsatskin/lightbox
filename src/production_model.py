class Production(object):
	"""docstring for production"""
	def __init__(self, total=0, length, time_unit, production_unit = "kWh", solar_array):
		super(Year, self).__init__()
		self.total = total
		self.production_unit = production_unit
		self.length = length
		self.time_unit = time_unit
		self.solar_array = solar_array

	def absolute_time():
		"""Returns length of period in seconds based on time unit"""
		return self.length*({
			'Year' : 3600*24*365
			'Month' : 3600*24*30 ##Simplification
			'Day' : 3600*24
			'Hour' : 3600
			'Minute' : 60
			'Second' : 1
			}[self.time_unit])

class Year(Production):
	"""docstring for Year"""
	def __init__(self, current_year, start_year, solar_array):
		super(Year, self).__init__(length = 12, time_unit = "Month", solar_array)
		self.current_year = current_year
		self.start_year = start_year

	def degradation():
		self.degradation = solar_array.tau**(self.current_year - self.start_year)

class Month(Production):
	"""docstring for Month"""
	def __init__(self, current_month, solar_array):
		super(Month, self).__init__(length = 30, time_unit = "Day", solar_array)
		self.current_month = current_month
		self.length = check_days()

	def check_days():
		return {
			"Jan" : 31
			"Feb" : 28
			"Mar" : 31
			"Apr" : 30
			"May" : 31
			"Jun" : 30
			"Jul" : 31
			"Aug" : 31
			"Sep" : 30
			"Oct" : 31
			"Nov" : 30
			"Dec" : 31
		}[current_month]

class Day(Production):
	"""docstring for Day"""
	def __init__(self, current_month, current_day, solar_array):
		super(Day, self).__init__( length = 24, time_unit = "Hour", solar_array)
		self.current_month = current_month
		self.current_day = current_day

class Hour(Production):
	"""docstring for Hour"""
	def __init__(self, current_month, current_day, current_hour, solar_array):
		super(Hour, self).__init__(length = 60, time_unit = "Minute")
		self.current_month = current_month
		self.current_day = current_day
		self.current_hour = current_hour

	def get_energy():
		time = string(current_hour) + "/" +  string(current_day) + "/" + string(current_month)
		##Pull historical data for 'time'
		##Pull efficiency information 




		


		
		
