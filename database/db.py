import json
import os

DATA_FILE = 'data/players.json'

def load_players():
    if not os.path.exists('data'):
        os.makedirs('data')
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_players(players):
    with open(DATA_FILE, 'w') as f:
        json.dump(players, f, indent=4)
