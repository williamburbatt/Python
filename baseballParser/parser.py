import csv
import json

csvfile = open('C:\\Users\\willi\\PycharmProjects\\baseballParser\\venv\\draftResults.csv', 'r')
jsonfile = open('C:\\Users\\willi\\PycharmProjects\\baseballParser\\venv\\draftResultsJSON.json', 'w')

fieldnames = ("Pick", "Position", "Player", "Team", "Bid", "Fantasy Team")
reader = csv.DictReader(csvfile, fieldnames)
jsonfile.write('[')
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n')
jsonfile.write(']')