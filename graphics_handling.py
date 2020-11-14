# INF 405 Team Project 1
# Jonah Wolmark and D'Awnna Williams

# main program will use this class to render graphics on screen

class GraphicsHandler:
	def __init__(self, stateWinners, bidenEVTotals, trumpEVTotals, bidenNationalWins, trumpNationalWins):
		self.stateWinners = stateWinners            # A dictionary that contains the candidate who won the most in each state/district.  Each key is a state name, each value is the candidate that had the most wins in that state.
		self.bidenEVTotals = bidenEVTotals          # A dictionary that contains the number of times that Biden got each EV total.  Keys are EV totals, values are the number of times Biden got that total.
		self.trumpEVTotals = trumpEVTotals			# Same as the bidenEVTotals, but for Trump.
		self.bidenNationalWins = bidenNationalWins	# The number of times that Biden got 270 or more electoral votes in a trial.
		self.trumpNationalWins = trumpNationalWins	# Same as bidenNationalWins, but for Trump.
		
		# TODO: Any code to set up the graphics library, pre-output goes here.

	def display(self):
		x = 0  # Placeholder line to prevent python from being upset about the formatting. Remove this when you start writing this function.

		# TODO: Any code to actually display stuff goes here.