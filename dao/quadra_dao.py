import json
from models.quadra import Quadra

QUADRAS_FILE = 'data/quadras.json'

def load_quadras():
    try:
        with open(QUADRAS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_quadras(data):
    with open(QUADRAS_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def get_all_quadras():
    data = load_quadras()
    return [Quadra(**item) for item in data]