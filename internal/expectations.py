import json

with open("./data/workouts.json", "r") as read_file:
    data = json.load(read_file)

def fetchSugar(exercice):
    parsed = data['workouts'][exercice]
    return parsed['sugar']['title']

def fetchPosition(exercice):
    parsed = data['workouts'][exercice]['position']
    positions = [(point['milieu_x'], point['milieu_y']) for point in parsed]
    return positions