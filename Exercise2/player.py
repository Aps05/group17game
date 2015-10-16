from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]
max_mass = 3000 #3k grams = 3kg
current_mass = 2300 #already holding 3 items