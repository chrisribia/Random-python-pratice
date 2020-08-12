# Create a list of casualties from battles
battleDeaths = [482, 93, 392, 920, 813, 199, 374, 237, 244]
# Create a function that updates all battle deaths by adding 100
def updated(x):     return x + 100
# Create a list that applies updated() to all elements of battleDeaths
updated = list(map(updated, battleDeaths))
list(map((lambda x: x + 100), battleDeaths))


firstLetter, secondLetter = 'Bark qwert'
print(firstLetter)
