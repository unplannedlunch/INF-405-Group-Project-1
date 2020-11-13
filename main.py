# INF 405 Team Project 1
# Jonah Wolmark and D'Awnna Williams

import election_objects

# Main program flow goes here

# TODO: Variables to aggregate data from all iterations
country = election_objects.CountryData()

numOfIterations = int(input("Choose a number of iterations for the simulation to run. Please enter only an integer value: "))
for i in range (0, numOfIterations):
    for state in country.states:
        print(state.name, state.ev, state.basePrediction)

# TODO: Display graphics (graphs, map, etc)