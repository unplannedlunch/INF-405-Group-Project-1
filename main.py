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

# Organize EVs into graph friendly dictionaries
bidenEVTotals = {}
trumpEVTotals = {}
for spread in evsPerIteration:
	#print(spread.get('Biden'), spread.get('Trump'))
	bidenEVTotals.update({spread.get('Biden'): bidenEVTotals.get(spread.get('Biden'), 0) + 1})
	trumpEVTotals.update({spread.get('Trump'): trumpEVTotals.get(spread.get('Trump'), 0) + 1})

# How many times did each candidate get over 270 EVs
bidenNationalWins = 0
trumpNationalWins = 0
nationalTies = 0

for ev, frequency in bidenEVTotals.items():
	if ev >= 270:
		bidenNationalWins += frequency

for ev, frequency in trumpEVTotals.items():
	if ev >= 270:
		trumpNationalWins += frequency

for ev, frequency in trumpEVTotals.items():
	if ev == 269:
		nationalTies += frequency

# Figure out who won each state more
stateWinners = {}
for state, timesWon in bidenStateWins.items():
	if timesWon > trumpStateWins.get(state, 0):
		stateWinners.update({state: 'Biden'})
	elif timesWon < trumpStateWins.get(state, 0):
		stateWinners.update({state: 'Trump'})
	else:
		stateWinners.update({state: 'Tie'})	
for state in trumpStateWins.items():
	if state[0] not in stateWinners:
		stateWinners.update({state[0]: 'Trump'})

# Print results to console
print('The candidate who won the most in each voting district are as follows:')
print(stateWinners)

print()

print('Biden got these EV Totals these amounts of times:')
print(bidenEVTotals)

print()

print('Trump got these EV Totals these amounts of times:')
print(trumpEVTotals)

print()

print('Biden got 270 EVs', bidenNationalWins, 'times.')
print('Trump got 270 EVs', trumpNationalWins, 'times.')
print('The candidates tied', nationalTies, 'times.')


# TODO: Display graphics (graphs, map, etc)