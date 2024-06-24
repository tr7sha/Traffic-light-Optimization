"""
MARKOV DECISION PROCESS (MDP) - FINAL PROJECT
---------------------------------------------
SUBJECT:        ARTIFICIAL INTELLIGENCE
"""

import csv
import itertools


def bellman_equations(state, iteration, state_value_list):

    costs_actions = []
    for index, element in enumerate(dictionaries):
        costs_actions.append(calculate_cost_directions(state, iteration, state_value_list, element,costs_for_actions[index]))

    bellman_equation = round(min(costs_actions), 6)

    for state_index, state_element in enumerate(initial_states_list):
        if state == state_element:
            state_value_list[state_index].append(bellman_equation)
    return state_value_list


def transition_tables_probability_counter(cardinal_directions):
    """Function to calculate all the probabilities for the transition table"""
    directions_dictionary = {}
    print("Transition table for %s:\n" % cardinal_directions)
    # for every possible combination
    for state in all_states_combinations:
        total_cases = 0
        # we iterate the rows with the data
        for r in rows:
            # for every row in our transition tables, we count all the occurrences
            # of it to calculate the probabilities
            # e.g. first row for green light in east 'E': H;H;H;E -> we count the rows and save it
            if (state[0] + cardinal_directions) in r[0]:
                total_cases = total_cases + 1
        # some combinations do not appear in data.csv, so they'd be 0.
        if total_cases != 0:
            # calculate the probability for every cell dividing it by the total cases for each row
            probability = rows.count([state[0] + cardinal_directions + state[1]]) / total_cases
        else:
            probability = 0
        directions_dictionary[state[0] + cardinal_directions + state[1]] = str(round(probability, 6))
        print(state[0] + cardinal_directions + state[1] + ': ' + str(round(probability, 6)) + " ("
              + str(round(probability*100, 2)) + "%)")

        # e.g. output:
        # High;High;High;E;High;High;High: 0.616438 (61.64%)
    return directions_dictionary


def calculate_cost_directions(state, iteration, state_value_list, dictionary, cost):
    """Cal"""
    result_cost = 0
    i = 0
    for item in dictionary:
        if state in item:
            result_cost = result_cost + float(dictionary[item])*state_value_list[i][iteration-1]
            i = i+1
    Exp_cost = cost + result_cost

    return Exp_cost


def optimal_policy_calculation(values_list):
    for index,state in enumerate(values_list):
        min_value = min(state)
        min_index = state.index(min_value)

        optimal_values_for_states.append(min(state))

        if min_index == 0:
            optimal_policy_result[initial_states_list[index]] = "E"
            optimal_actions_for_states.append("E")
        if min_index == 1:
            optimal_policy_result[initial_states_list[index]] = "N"

            optimal_actions_for_states.append("N")
        if min_index == 2:
            optimal_policy_result[initial_states_list[index]] = "W"

            optimal_actions_for_states.append("W")


def optimal_value_calculation():
    for index,state in enumerate(initial_states_list):
        optimal_value_E = optimal_policy(state, optimal_policy_list, dictionaries[0],costs_for_actions[0])
        optimal_value_N = optimal_policy(state, optimal_policy_list, dictionaries[1],costs_for_actions[1])
        optimal_value_W = optimal_policy(state, optimal_policy_list, dictionaries[2],costs_for_actions[2])
        optimal_value_list.append([optimal_value_E,optimal_value_N,optimal_value_W])


def optimal_policy(state ,optimal_policy_list,dictionary, cost):
    result = 0
    i = 0
    for item in dictionary:
        if state in item:

            result = result + float(dictionary[item])*optimal_policy_list[i]

            i = i+1

    exp_cost = cost + result

    return exp_cost



# First, we define the two lists with the combinations for the transition tables of our MDP
initial_states_list = ['High;High;High;', 'High;High;Low;', 'High;Low;High;', 'High;Low;Low;', 'Low;High;High;',
                       'Low;High;Low;', 'Low;Low;High;', 'Low;Low;Low;']
final_states_list = [';High;High;High', ';High;High;Low', ';High;Low;High', ';High;Low;Low', ';Low;High;High',
                     ';Low;High;Low', ';Low;Low;High', ';Low;Low;Low']

# Then, we define the costs for every action.
costs_for_actions = [20, 20, 20]

# Then, we do a cartesian product to obtain all the possible combinations for the transition tables
all_states_combinations = list(itertools.product(initial_states_list, final_states_list))

print("<-----------MARKOV DECISION PROCESS MODEL------------>")
print("States: N(High/Low), E(High/Low), W(High/Low)")
print("Actions:")
print("Turn_green_north()")
print("Turn_green_east()")
print("Turn_green_west()")
print("All possible combinations for states:\n", all_states_combinations)  # len: 64 possible combinations

# ##################################### READING FILES ######################################
# rows defined to save all the .csv data
rows = []
# reading the csv file
with open('data/Data.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names for first row
    fields = next(csvreader)
    # extracting each data row by row
    for row in csvreader:
        rows.append(row)
    # get total number of rows
    print("Total nr. of rows of DATA with header: %d" % csvreader.line_num)

# printing the field names
print('Field names are:\n' + ', '.join(field for field in fields))

# ##################################### READING FILES ######################################
# We define the directions and call the transition table calculator function for each of them
directions = ['E', 'N', 'W']
# We save the data in dictionaries for each direction
dictionaries = []

# Creating a dictionary for every transition table
for direction in directions:
    dictionaries.append(transition_tables_probability_counter(direction))

# We save the bellman eq´s result for every state
state_value_list = [[0], [0], [0], [0], [0], [0], [0], [0]]

# Flags for every state to save when the values are repeating in the bellman eqs
repeated_flags_list = []

# We initialize the flags to false
for state in initial_states_list:
    repeated_flags_list.append(False)

repeated_flag = False
# We define the iterations for the bellman equations
iterations = 1

# We start to calculate the bellman eqs. until all the values for all the states gets repeated
while not repeated_flag:
    for state in initial_states_list:
        bellman_equations(state, iterations, state_value_list)
    for index, state in enumerate(initial_states_list):
        if state_value_list[index][iterations] == state_value_list[index][iterations-1]:
            repeated_flags_list[index] = True

    if False not in repeated_flags_list:
        repeated_flag = True
    iterations = iterations + 1

print("Last iteration:", iterations)

# We print the bellman eqs
print("Bellman equations:", iterations)
for element in state_value_list:
    print(element)

# List for saving the optimal policies
optimal_policy_list = []

# We append the last elements for every state in the optimal policy list
for element in state_value_list:
    optimal_policy_list.append(element[-1])

optimal_value_list = []

optimal_value_calculation()

optimal_values_for_states = []
optimal_actions_for_states = []
optimal_policy_result = {}
optimal_policy_calculation(optimal_value_list)

print("Optimal Values:")
for index, state in enumerate(initial_states_list):
    print("For state: %s = %f" %(state, optimal_policy_list[index]))
# print(optimal_policy_list)
print("Optimal Policy Final Results")
print(optimal_policy_result)


