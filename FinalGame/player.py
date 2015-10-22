from items import *
from map import *

# Global variable, displays victory screen and stops the game when set to True
victory = False
# Global variable, displays defeat screen and stops the game when set to True
defeat = False

player = {
    # Start game at the reception
    "current_room": rooms["Atrium"],
    # Saving last room player was in
    "previous_room": rooms["Atrium"],

    # Start with an empty inventory
    "inventory": [item_crucifix],
    # The number of items the player can hold at any one time
    "inv_space": 6,

    # Initialising sanity, health and faith values
    "health": 100,
    "sanity": 100,
    
    # The player might want to try and fight the monster with his fists. Who are we to judge...
    "power": 10
}