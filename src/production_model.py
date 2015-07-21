import Efficiency

class Production(object):
	"""docstring for production"""
	def __init__(self, length, solar_array, time_unit, total=0, production_unit = "kWh"):
		super(Year, self).__init__()
		self.total = total
		self.production_unit = production_unit
		self.length = length
		self.time_unit = time_unit
		self.solar_array = solar_array

	def absolute_time():
		"""Returns length of period in seconds based on time unit"""
		return self.length*({
			'Year' : 3600*24*365,
			'Month' : 3600*24*30, 
			'Day' : 3600*24,
			'Hour' : 3600,
			'Minute' : 60,
			'Second' : 1
			}[self.time_unit])

class Year(Production):
	"""docstring for Year"""
	def __init__(self, current_year, start_year, solar_array):
		super(Year, self).__init__(solar_array, length = 12, time_unit = "Month")
		self.current_year = current_year
		self.start_year = start_year

	def degradation():
		self.total = solar_array.tau**(self.current_year - self.start_year)*self.total

	def set_production():
		self.production = []
		for i in range(length):
			M = Month(str(i+1), self.solar_array)
			M.set_production()
			self.production[i] = M.production
		self.get_total()

	def set_total():
		sum_p = 0
		for p in self.production:
			sum_p = sum_p + p
		self.total = sum_p 	

		
	
class Month(Production):
	"""docstring for Month"""
	def __init__(self, current_month, solar_array):
		super(Month, self).__init__(solar_array, length = 30, time_unit = "Day")
		self.current_month = current_month
		self.length = check_days()

	def check_days():
		return {
			"1" : 31,
			"2" : 28,
			"3" : 31,
			"4" : 30,
			"5" : 31,
			"6" : 30,
			"7" : 31,
			"8" : 31,
			"9" : 30,
			"10" : 31,
			"11" : 30,
			"12" : 31
		}[current_month]

	def set_production():
		self.production = []
		for i in range(length):
			D = Day(str(i+1), self.solar_array)
			D.set_production()
			self.production[i] = D.production
		self.set_total()

	def set_total():
		sum_p = 0
		for p in self.production:
			sum_p = sum_p + p
		self.total = sum_p		

class Day(Production):
	"""docstring for Day"""
	def __init__(self, current_month, current_day, solar_array):
		super(Day, self).__init__(solar_array, length = 24, time_unit = "Hour")
		self.current_month = current_month
		self.current_day = current_day

	def set_production():
		self.production = []
		for i in range(length):
			H = Hour(str(i+1), self.solar_array)
			H.set_production
			self.production[i] = H.production
		self.get_total()
		
	def set_total():
		sum_p = 0
		for p in self.production:
			sum_p = sum_p + p
		self.total = sum_p


class Hour(Production):
	"""docstring for Hour"""
	def __init__(self, current_month, current_day, current_hour, solar_array):
		super(Hour, self).__init__(solar_array, length = 60, time_unit = "Minute")
		self.current_month = current_month
		self.current_day = current_day
		self.current_hour = current_hour

	def set_production():
		time = string(current_hour) + "/" +  string(current_day) + "/" + string(current_month)
		##Pull historical data for 'time'
		self.temperature
		self.flux
		##Pull efficiency information
		self.efficiency = Efficiency(self.solar_array.solar_panel, self.temperature, self.current_hour)
		self.solar_power = self.flux*self.solar_array.array_area
		self.production = self.efficiency.efficiency*self.solar_power



		


		
		
