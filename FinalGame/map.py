from items import *
from enemies import *

room_atrium = {
    "id": "Atrium",
    
    "name": "Hospital Atrium",

    "description":
    """You are in the atrium of what looks like an old hospital. You see that 
there are, above in the distance, lights, but when you try the switch nothing
happens. Your only light comes through small dingy windows. All the furniture 
is upturned but the desk catches your eye, it's covered in scratchmarks. Human 
scratchmarks. There are several exits from the atrium: you can go down to the basement
via a service elevator but you see on the door in what appears to be blood the message:
'Only venture down weilding defence or your life'. To your east is a canteen, 
maybe you fancy a bite to eat? To your West is the main ward... and finally, you 
see a spiral staircase leading up has been signposted 'Psychiatric Reception.'
You really are out of your comfort zone.""",

    "look": "This is the room you started in, or at least you think it is.",

    "exits": {"down": "Basement", "east": "Canteen", "west": "Ward", "up": "Reception", "south": "Exit"},

    "items": [item_letter, item_notepad, item_note1],

    "requirements": [],

    "enemies": []
}

room_reception = {
    "id": "Reception",

    "name": "the Psychiatric Reception",

    "description":
    """You are in the Psychiatric Reception. It's very bare and the only light 
is a small cracked window. By the marks on the floor it looks like the desk
had been dragged infront of the door to the north, it's labelled 'ISOLATION'.
But the desk is now in two... Something with immense force, came through that
door and has left it open for travel... So to the north you have the 
isolation, but looks like something has escaped. You have long term care 
to the east down a very long corridor, you'd call it a tunnel into darkness.
You have the stairs back down to the atrium.""",

    "look": "Looking carefully into the psychiatric reception.",

    "exits":  {"north": "Isolation", "down": "Atrium", "east": "Care"},

    "items": [item_bible, item_crucifix],

    "requirements": [item_shoes],

    "enemies": []
}

room_isolation = {
    "id": "Isolation",
    
    "name": "the Isolation Rooms",

    "description":
    """You are in the Isolation rooms. You can close your eyes and feel the
screams of tourment as helpless people were locked in small white 
rooms to live out their days. The only light is what reflects from the 
reception. You trip over. You land in a puddle, you can't see what it is,
but it's too thick to be water... To the north you see a sign saying 
'Electro-shock therapy'. As you get closer there is a ghostly chill. To the
east there is the long term care unit. Back to the light in the south 
there is the reception.""",

    "look": "You apprehensively peek into the eerie isolation rooms, it looks safe.",

    "exits": {"north": "Electro", "south": "Reception", "east": "Care"},

    "items": [item_water],

    "requirements": [],

    "enemies": []
}

room_care = {
    "id": "Care",
    
    "name": "Long Term Care",

    "description":
    """You are in the Long Term care ward. This room is quite bright, all the 
curtains have been torn down. As you begin to walk in the weather outside 
becomes very dark... You can see where all the beds once lay neatly, but 
they've all been dragged into a corner. A child would call it a play fort, you
would see it as protection... To the west you have the dark horrors of the
Isolation rooms. To the south you have the dim corridor back to reception.""",

    "look": """The sign for the long-term care room looks intact. You can’t hear
anything crawling around, so assume you it is safe.""",

    "exits": {"west": "Isolation", "south": "Reception"},

    "items": [item_clue2],

    "requirements": [],

    "enemies": []
}

room_electro = {
    "id": "Electro",
    
    "name": "Electro-Shock Therapy",

    "description":
    """You are in the treatment room for Electro-shock therapy. There is a 
freezing ghostly chill. The room is bare, just a chair in the middle. It
has restraints on but it appears as if someone or something broke out of 
them. There is a single window at the back of the room but is crusted with 
a sulphur like substance... The only exit is back to the south to Isolation.""",

    "look": "This room looks disturbing. There is a small cracked glass window.",

    "exits": {"south": "Isolation"},

    "items": [item_note4, item_torch],

    "requirements": [],

    "enemies": [enemy_mutant]
}

room_canteen = {
    "id": "Canteen",
    
    "name": "the Canteen",
    
    "description":
    """You are in the Canteen. It is an old style servery, it smells like your 
primary school dinners. You see a cupboard slightly ajar. You open it and a 
stream of rats comes out which you jump from. They run towards a grand fire 
place. Once they clear you see they were feasting on scraps of flesh on a 
bone. It looks famiiar... To the west is the Atrium. To the east leads a 
small passage through to the dining hall.""",

    "look": "Peeking through an ajar door.",
    
    "exits": {"west": "Atrium", "east": "Dining"},

    "items": [item_beans, item_knife],

    "requirements": [],

    "enemies": []
}

room_dining = {
    "id": "Dining",
    
    "name": "the Dining Room",
    
    "description":
    """You are in the Dining room. It is very grand, it has 3 large chandeliers
and stained glass windows around the side. But once you look down it's less
beautiful, all the tables are upturned or broken. At the far end of the room 
you see a table on its side and 4 kitchen knifes, which have been thrown into the 
side of it... To the west you have the small passage back to the canteen.""",

    "look": """There are broken oak frames surround the front of the dining room.
This room looks bountiful, but you wonder if it is guarded by a mutant.""",
    
    "exits": {"west": "Canteen"},

    "items": [item_axe, item_note2, item_beans],

    "requirements": [],

    "enemies": [enemy_ghost]
}

room_ward = {
    "id": "Ward",
    
    "name": "Ward 1",
    
    "description":
    """You are in the ward. As you walk in you feel unnerved, in the back of 
your mind you feel like something horrible happened here. There are about 
30 beds, all have them have been destroyed apart from one. Just off the 
centre of the room is a bed, chair and table sitting perfectly... On the table
there is a vase of flowers and they look fresh? To your west are double 
doors that lead to the Intensive Care Unit. To the east leads back to the 
Atrium.""",

    "look": """Through the glass walls of ward 1, you notice it is completely empty,
apart from bloody bed sheets and broken medical equipment.""",
    
    "exits": {"west": "Icu", "east": "Atrium"},

    "items": [item_key],

    "requirements": [],

    "enemies": []
}

room_icu = {
    "id": "Icu",
    
    "name": "the ICU",
    
    "description":
    """You are in the ICU. There are four beds with life support. As you walked 
in you think you hear the life support going and see 4 bodies in the beds,
you blink and they are gone. 2 of the beds still have blood stained sheets 
on... The door to the north has bed wheel tracks marked in blood going under
the door, this leads to the morgue, the windows in the door look frozen. To 
east you have the ward.""",

    "look": """As you peek your head through the double doors, you can see inside
the ICU room.""",
    
    "exits": {"north": "Morgue", "east": "Ward"},

    "items": [item_note3, item_medicine],

    "requirements": [],

    "enemies": [enemy_ghost]
}

room_morgue = {
    "id": "Morgue",
    
    "name": "the Morgue",
    
    "description":
    """You are in the morgue. It is ice cold and you are shivering. You hear a 
loud bang from one of the body chambers and as you turn it is open... There
is a blood stained slab in the centre and next to it lies a tray of doctors tools 
of the trade, but you get the sense the trade might have not on the dead. 
You really feel like running from this room with shivers down your spine.
To the south is the only exit back to the ICU.""",
    # What does this mean (the last line mostly)? 
    # There is a blood stained slab in the centre and next to it lies a tray of doctors tools 
    # of the trade, but you get the sense the trade might have not on the dead. 
    
    "look": """The morgue looks horrific and will most likely lower your sanity 
by venturing into the room""",    
    
    "exits": {"south": "Icu"},

    "items": [item_medicine,item_clue1, item_shoes],

    "requirements": [],

    "enemies": [enemy_mutant]
}

room_basement = {
    "id": "Basement",
    
    "name": "the Basement",
    
    "description":
    """You have come down the service elevator, the only light is that of your 
torch. It looks like a workshop, but when you look closely you can see little
bits of padding to the left of the walls. It looks like this might have containined
isolation rooms. You imagine the suffering of the patients locked up in the 
darkness... There is a concealed door to the east and you hear a distance 
banging. On the door it says 'FEAR ME' in what looks like blood. You are sure 
you can get through though, or back up the service elevator to the Atrium.""",

    "look": """You can’t see anything in the basement, but you assume it is dark.
You can see engravings of 0s and 1s on the lift shaft.""",
    
    "exits": {"up": "Atrium", "east": "Dmorgue"},

    "items": [item_note5, item_beans],

    "requirements": [item_torch, item_key],

    "enemies": [enemy_mutant]
}

room_dmorgue = {
    "id": "Dmorgue",
    
    "name": "the Disused Morgue",
    
    "description":
    """The door creaks open and you walk into the eerie disued morgue. Although
you soon belive it's not that disused as on the slab in the middle there lies
a body... It doesnt appear to be decomposing and it smells musty, not rotting.
You don't understand what is going on here, fear begins to overwhelm you. You 
look around and all the body chambers seem full? Dread fills your body. The 
only exit is west back to the basement.""",

    "look": """Looking from the basement into this room, you are filled with fear.
You know your sanity level will seriously drop if you enter the room.""",
    
    "exits": {"west": "Basement"},

    "items": [item_note6, item_medicine, item_medicine, item_clue3],

    "requirements": [],

    "enemies": [enemy_mutant]
}

room_exit = {
    "id": "Exit",
    
    "name": "the only exit from this hospital.",
    
    "description":
    """No Description Yet""",
    
    "look": """A big metal door. It looks unbreakable, though it looks like there
are scratches on its surface. It doesn't have a key lock. Instead, it requires a code
combination to open. They key pad has only 2 buttons for the code, 0 and 1. Strange...""",

    "exits": {},

    "items": [],

    "requirements": [],

    "enemies": [],
    
    "combination": finalCode
}

rooms = {
    "Atrium": room_atrium,
    "Reception": room_reception,
    "Isolation": room_isolation,
    "Care": room_care,
    "Electro": room_electro,
    "Canteen": room_canteen,
    "Dining": room_dining,
    "Ward": room_ward,
    "Icu": room_icu,
    "Morgue": room_morgue,
    "Basement": room_basement,
    "Dmorgue": room_dmorgue,
    "Exit": room_exit
}