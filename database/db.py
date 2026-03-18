import json
import os

FILE = "data.json"

# load data
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        users = json.load(f)
else:
    users = {}


def save_data():
    with open(FILE, "w") as f:
        json.dump(users, f)
