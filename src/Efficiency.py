class Efficiency(object):
	"""docstring for Efficiency"""
	def __init__(self, solar_panel, temperature, hour):
		super(Efficiency, self).__init__()
		self.solar_panel = solar_panel
		self.base_efficiency = solar_panel.efficiency
		self.hour = hour

	def get_model():
		##Grab model parameters
		self.temp_coeff
		self.temp_intcpt
		self.temperature = self.temperature*self.temp_coeff + self.temp_intcpt
		self.temperature_efficiency  = self.solar_panel.beta*(self.solar_panel.base_temp - temperature)
		
		self.hourly_shading
		self.shading_efficiency = self.hourly_shading[self.hour]*self.solar_panel.phi 
		 

	def set_efficiency():
		self.efficiency = self.base_efficiency*self.shading_efficiency*self.temperature_efficiency




		