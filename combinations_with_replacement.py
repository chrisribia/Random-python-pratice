from itertools import combinations_with_replacement

# Create a list of objects to combine
list_of_objects = ['warplanes', 'armor', 'infantry']

# Create an empty list object to hold the results of the loop
combinations = []
for i in list(range(len(list_of_objects))):
    combinations.append(combinations_with_replacement(list_of_objects, i+1))


combinations = [i for row in combinations for i in row]

# View the results
print(combinations)
