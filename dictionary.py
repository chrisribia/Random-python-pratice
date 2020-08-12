importers = {'El Salvador' : 1234,
             'Nicaragua' : 152,
             'Spain' : 252
            }

exporters = {'Spain' : 252,
             'Germany' : 251,
             'Italy' : 1563
             }


# Find the intersection of importers and exporters
intersection = importers.keys() & exporters.keys()
# Find the difference between importers and exporters
difference = importers.keys() - exporters.keys()
# Find countries where the amount of exports matches the amount of imports
item = importers.items() & exporters.items()
print(item)