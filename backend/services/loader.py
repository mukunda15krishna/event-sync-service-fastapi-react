import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_crm():
    path = os.path.join(DATA_DIR, "crm_events.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def load_calendar():
    path = os.path.join(DATA_DIR, "calendar_events.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)