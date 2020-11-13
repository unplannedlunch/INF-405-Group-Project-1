# INF 405 Team Project 1
# Jonah Wolmark and D'Awnna Williams

import csv
import re
import random

class CountryData:
	def __init__(self):
		self.states = []
		self._populate()

	def _populate(self):
		# Read from data file and store in this class
		with open('2020-presidential.csv', newline = '') as file:
			csvReader = csv.reader(file)
			for row in csvReader:

				# Discards header row and any row that contains a candidate other than Biden or Trump, and a forecast date that is not the most recent in the file. Also if it is US as state.
				if(row[1] == 'US' or (re.search('forecast', row[0]) or not (re.search('10/06/20', row[0]) and (re.search('Biden', row[4]) or re.search('Trump', row[4]))))):
					continue

				currentState = None

				# Checks if state is already in list
				for state in self.states:
					if state.name == row[1]:
						currentState = state
						currentState._setBasePrediction(currentState.getBasePrediction() - float(row[8]))
						break

				# Ensures that currentState is never null
				if currentState is None:
					currentState = State(row[1], int(row[2]), float(row[8]))
					self.states.append(currentState)

class State:
	def __init__(self, name, ev, basePrediction):
		self.name = name
		self.ev = ev
		self.basePrediction = basePrediction
	
	def getBasePrediction(self):
		return self.basePrediction
	
	def _setBasePrediction(self, bp):
		self.basePrediction = bp
	
	# Behaves as outlined in assignement documentation
	def generateCandidateSelectionWithVariance(self):
		marginOfError = 3.0
		randomNoise = random.normalvariate(0.0, 1.0) / 2.0 * marginOfError
		finalPrediction = self.basePrediction + randomNoise
		return ('Trump', 'Biden')[finalPrediction >= 0]