import json


def git_candidates():
    with open('candidates.json', "r", encoding="UTF-8") as file:
        candidates_json = json.load(file)
        return candidates_json
