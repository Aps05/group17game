from items import *

room_atrium = {
    "id": "Atrium",
    
    "name": "Hospital Atrium",

    "description":
    """You are in the atrium of what looks like an old hospital. You see that 
    there are, above in the distance, lights but when you try the switch nothing
    happens. Your only light comes through small dingy windows. All the furniture 
    is upturned but the desk catches your eye, it's covered in scratchmarks. Human 
    scratchmarks. There are several exits from atrium: you can do down to the basement
    via a service elevator but you see on the door in what appears to be blood the message 
    'Only venture down weilding defence or your life'. To you're east is a canteen, 
    maybe you fancy a bite to eat? to your West is the main ward... and finally you 
    see a spiral staircase leading up has been signposted 'Psychiatric Reception.
    You really are out of your comfort zone.""",

    "exits": {"down": "Basement", "east": "Canteen", "west": "Ward", "up": "Reception"},

    "items": [item_biscuits, item_handbook]
}

room_reception = {
    "id": "Reception",

    "name": "the Psychiatric Reception",

    "description":
    """You are in the Psychiatric Reception. It's very bare and the only light 
    is a small cracked window. By the marks on the floor it looks like the desk
    had been dragged infront on the door to the north, it's labelled 'ISOLATION'.
    But the desk is now in two... Something with immense force, came through that
    door and has left it open for travel... So to the north you have the 
    isolation, but looks like something has escaped. You have long term care 
    to the east down a very long corridor, you'd call it a tunnel into darkness.
    You have the stairs back down to the atrium.""",

    "exits":  {"north": "Isolation", "down": "Atrium", "east": "Care"},

    "items": []
}

room_isolation = {
    "id": "Isolation",
    
    "name": "the Isolation Rooms",

    "description":
    """You are in the Isolation rooms. You can close your eyes and feel the
    screams of tourment as helpless people were locked in there small white 
    rooms to live out their days. The only light is what reflects from the 
    reception. You trip over. You lad in a puddle, you can't see what it is,
    but it's too thick to be water... To the north you see a sign saying 
    'Electro-shock therapy' as you get closer there is a ghostly chill. To the
    east there is the long term care unit. Back to the light in the south 
    there is the reception."",

    "exits": {"north": "Electro", "south": "Reception", "east": "Care"},

    "items": []
}

room_care = {
    "id": "Care",
    
    "name": "Long Term Care",

    "description":
    """No description yet.""",

    "exits": {"west": "Isolation", "south": "Reception"},

    "items": []
}

room_electro = {
    "id": "Electro",
    
    "name": "Electro-Shock Therapy",

    "description":
    """No description yet.""",

    "exits": {"south": "Isolation"},

    "items": [item_pen]
}

room_canteen = {
    "id": "Canteen",
    
    "name": "the Canteen",
    
    "description":
    """No description yet.""",
    
    "exits": {"west": "Atrium", "east": "Dining"},

    "items": []
}

room_dining = {
    "id": "Dining",
    
    "name": "the Dining Room",
    
    "description":
    """No description yet.""",
    
    "exits": {"west": "Canteen"},

    "items": []
}

room_ward = {
    "id": "Ward",
    
    "name": "Ward 1",
    
    "description":
    """No description yet.""",
    
    "exits": {"west": "Icu", "east": "Atrium"},

    "items": []
}

room_icu = {
    "id": "Icu",
    
    "name": "the ICU",
    
    "description":
    """No description yet.""",
    
    "exits": {"north": "Mourge", "east": "Ward"},

    "items": []
}

room_mourge = {
    "id": "Mourge",
    
    "name": "the Mourge",
    
    "description":
    """No description yet.""",
    
    "exits": {"south": "Icu"},

    "items": []
}

room_basement = {
    "id": "Basement",
    
    "name": "the Basement",
    
    "description":
    """No description yet.""",
    
    "exits": {"up": "Atrium", "east": "Dmourge"},

    "items": []
}

room_dmourge = {
    "id": "Dmourge",
    
    "name": "the Disused Mourge",
    
    "description":
    """No description yet.""",
    
    "exits": {"west": "Basement"},

    "items": []
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
    "Mourge": room_mourge,
    "Basement": room_basement,
    "Dmourge": room_dmourge
}