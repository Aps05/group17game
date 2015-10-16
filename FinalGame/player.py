from items import *
from map import rooms

inventory = []

# Start game at the reception
current_room = rooms["Atrium"]

def new_game():
    global inventory
    global current_room
    
    inventory = []

    # Start game at the reception
    current_room = rooms["Atrium"]