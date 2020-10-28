class CountryData:
	def __init__(self):
		self.states = []
		self._populate()

	def _populate(self):
		#Read from data file and store in this class
		print()

class State:
	def __init__(self, name, ev, basePrediction):
		self.name = name
		self.ev = ev
		self.basePrediction = basePrediction