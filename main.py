# INF 405 Team Project 1
# Jonah Wolmark and D'Awnna Williams

import election_objects

# Variables to aggregate data
country = election_objects.CountryData()
evsPerIteration = []
bidenStateWins = {}
trumpStateWins = {}

# Core program loop
numOfIterations = int(input("Choose a number of iterations for the simulation to run. Please enter only an integer value: "))
for i in range (0, numOfIterations):
	bidenEVs = 0
	trumpEVs = 0
	for state in country.states:
		winner = state.generateCandidateSelectionWithVariance()
		if winner == 'Biden':
			bidenEVs += state.ev
			bidenStateWins.update({state.name: bidenStateWins.get(state.name, 0) + 1})
		elif winner == 'Trump':
			trumpEVs += state.ev
			trumpStateWins.update({state.name: trumpStateWins.get(state.name, 0) + 1})
		else:
			print("THIS SHOULD NOT HAPPEN", state.name)
		evsPerIteration.append({'Biden': bidenEVs, 'Trump': trumpEVs})

# Process Data
bidenNationalWins = 0
trumpNationalWins = 0
nationalTies = 0

if(bidenEVs > trumpEVs):
	bidenNationalWins += 1
elif(trumpEVs > bidenEVs):
	trumpNationalWins += 1
else:
	nationalTies += 1

# Print results to console
print(bidenStateWins)
print(trumpStateWins)
print(bidenNationalWins, trumpNationalWins, nationalTies)

# TODO: Display graphics (graphs, map, etc)