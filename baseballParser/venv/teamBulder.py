import json

with open('C:\\Users\\willi\\PycharmProjects\\baseballParser\\venv\\draftResultsJSON.json', 'r') as data_file:
    json_data = data_file.read()

data = json.loads(json_data)

for player in data:
    print (player['Player'])