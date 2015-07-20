class Efficiency(object):
	"""docstring for Efficiency"""
	def __init__(self, solar_panel, temperature, hour):
		super(Efficiency, self).__init__()
		self.solar_panel = solar_panel
		self.base_efficiency = solar_panel.efficiency

	def get_model():
		##Grab model parameters
		self.shading_efficiency ##based on hour of day and panel coeff
		self.temperature_efficiency ##based on temperature reading and panel coeff

	def calc_efficiency():
		self.efficiency = self.base_efficiency*self.shading_efficiency*self.temperature_efficiency



		