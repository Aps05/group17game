from items import *
from map import rooms

player = {
    # Start game at the reception
    "current_room": rooms["Atrium"],

    # Start with an empty inventory
    "inventory": [],

    # Initialising sanity, health and faith values
    "health": 100,
    "sanity": 100,
    "faith": 100
}



def new_game():
    global inventory
    global current_room
    
    inventory = []

    # Start game at the reception
    current_room = rooms["Atrium"]