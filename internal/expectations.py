import json

with open("./data/workouts.json", "r") as read_file:
    data = json.load(read_file)

def fetchSugar(exercice):
    """
    Recovers the title associated with an exercice's sugar

    :param exercise: The name of the exercise
    :return: The title of the exercice
    """
    parsed = data['workouts'][exercice]
    return parsed['sugar']['title']

def fetchPosition(exercice):
    """
    Retrieves the positions of the points to display on the graph

    :param exercise: The name of the exercise
    :return: The positions of the points to display
    """
    parsed = data['workouts'][exercice]['position']
    positions = [(point['milieu_x'], point['milieu_y']) for point in parsed]
    return positions