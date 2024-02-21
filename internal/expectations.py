import json  # Importing the json module

with open("./data/workouts.json", "r") as read_file:
    data = json.load(read_file)

# Fetching exercise title
def fetchSugar(exercise):
    parsed = data['workouts'][exercise]
    return parsed['sugar']['title']

# Fetching exercise positions
def fetchPosition(exercise):
    parsed = data['workouts'][exercise]['position']
    positions = [(point['center_x'], point['center_y']) for point in parsed]
    return positions