from items import *
from map import rooms

player = {
    # Start game at the reception
    "current_room": rooms["Atrium"],
    # Saving last room player was in
    "previous_room": rooms["Atrium"],

    # Start with an empty inventory
    "inventory": [],

    # Initialising sanity, health and faith values
    "health": 100,
    "sanity": 100,
    "faith": 50,
    
    # The player could try and use his fists to fight off enemies... Who are we to judge
    "power": 10
}

def new_game():
    global inventory
    global current_room
    
    inventory = []

    # Start game at the reception
    current_room = rooms["Atrium"]