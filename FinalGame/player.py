from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Atrium"]

def new_game():
    global inventory
    global current_room
    
    inventory = [item_id, item_laptop, item_money]

    # Start game at the reception
    current_room = rooms["Atrium"]