import csv
import json

csvfile = open('draftResults.csv', 'r')
jsonfile = open('draftResultsJSON.json', 'w')

fieldnames = ("Pick", "Position", "Player", "Team", "Bid", "Fantasy Team")
reader = csv.DictReader(csvfile, fieldnames)
jsonfile.write('[')
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n')
jsonfile.write(']')