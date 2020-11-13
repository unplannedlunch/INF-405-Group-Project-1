# INF 405 Team Project 1
# Jonah Wolmark and D'Awnna Williams

import election_objects

# Main program flow goes here

# TODO: Variables to aggregate data from all iterations
country = election_objects.CountryData()
bidenNationalWins = 0
trumpNationalWins = 0
nationalTies = 0
bidenStateWins = {}
trumpStateWins = {}

numOfIterations = int(input("Choose a number of iterations for the simulation to run. Please enter only an integer value: "))
for i in range (0, numOfIterations):
	bidenEVs = 0
	trumpEVs = 0
	for state in country.states:
		winner = state.generateCandidateSelectionWithVariance()
		if winner == 'Biden':
			#print(state.name)
			bidenEVs += state.ev
			bidenStateWins.update({state.name: bidenStateWins.get(state.name, 0) + 1})
		elif winner == 'Trump':
			#print(state.name)
			trumpEVs += state.ev
			trumpStateWins.update({state.name: trumpStateWins.get(state.name, 0) + 1})
		else:
			print("THIS SHOULD NOT HAPPEN", state.name)
	#print("biden evs:", bidenEVs, "trump evs:", trumpEVs)
	if(bidenEVs > trumpEVs):
		bidenNationalWins += 1
	elif(trumpEVs > bidenEVs):
		trumpNationalWins += 1
	else:
		nationalTies += 1

print(bidenStateWins)
print(trumpStateWins)
temp = bidenStateWins.copy()
temp.update(trumpStateWins)
print(len(temp), sum(bidenStateWins.values()) + sum(trumpStateWins.values()))
print(bidenNationalWins, trumpNationalWins, nationalTies)

# TODO: Display graphics (graphs, map, etc)