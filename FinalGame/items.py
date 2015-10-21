import random
from binaryConverter import *


# Stores the sum of all numbers from the notes
sumOfNotes = 0
# In case of negative sum, 0 indicates Sign and Magnitude, 1 indicated Two's Complement
method = 0
# Used to store the final code required to win the game in binary form
finalCode = 0

# A sum of 0 would make the game too easy, so we generate new numbers in that case
while sumOfNotes == 0:
    note1 = random.randrange(-100, 100)
    note2 = random.randrange(-100, 100)
    note3 = random.randrange(-100, 100)
    note4 = random.randrange(-100, 100)
    note5 = random.randrange(-100, 100)
    note6 = random.randrange(-100, 100)
    # Adding all game notes in a list
    notes = [note1, note2, note3, note4, note5, note6]
    # Getting the sum the numbers on the notes
    for item in notes:
        sumOfNotes += item

if sumOfNotes > 0:
    # Convert to binary
    finalCode = convertToBinary(sumOfNotes)
else:
    # In case of negative, randomising wether the system should use sign and 
    # magnitude or two's complement
    method = random.randrange(0, 1)
    if method == 0:
        # Use Sign and Magnitude
        finalCode = convertToSignMagnitude(sumOfNotes)
    else:
        # Use Two's Complement
        finalCode = convertToTwosComplement(sumOfNotes)

item_torch = {
    "id": "torch",

    "name": "a torch",

    "description":
    """An old style black security torch. The bulb seems to flicker but it'll 
do the job in a dark room.""",
    
    "usable": False,
    # Items that can't be used as weapons has 0 power
    "power": 0
}

item_axe = {
    "id": "axe",

    "name": "an axe",

    "description":
    """ An old fire axe. Doesn't look sharp enough to break down a door anymore
but would do some serious damage to someone if they got in the way of it!""",
    
    "usable": False,
    
    "power": 50
}

item_salt = {
    "id": "salt",

    "name": "salt",

    "description":
    """A bottle of sea salt used by a chef once upon a time... It reminds you of
a book you once read that salt can be used to protect yourself from evil 
spirits!""",
    
    "usable": False,
    
    "power": 0
}

item_bible = {
    "id": "bible",

    "name": "The Holy Bible",

    "description": 
    """A copy of the Holy Bible. You can read the scriptures to learn of the 
miracles of the Lord and increase your faith. It will only work for so long""",
    
    "usable": False,
    
    "power": 0
}

item_knife = {
    "id": "knife",
    
    "name": "a sharp knife",

    "description":
    """A sharp kitchen knife. It gleams in the light. You need to hold it 
carefully, it could do some real damage to yourself and others""",
    
    "usable": False,
    
    "power": 30
}

item_water = {
    "id": "water",
    
    "name": "a bottle of Holy water",

    "description":
    """You pick up some water with a small crucifix in, you determine it's Holy 
water. You are aware from a book that it can be used to fight daemons.""",
    
    "usable": True,
    
    "power": 0
}

item_crucifix = {
    "id": "crucifix",
    
    "name": "a Crucifix",

    "description":
    """The is a small wooden crucifix with a model of Christ on it. You know 
that this has great power and can be used to drive away Evil.""",
    
    "usable": False,
    
    "power": 0
}

item_key = {
    "id": "key",
    
    "name": "a rusty key",

    "description":
    """A rusty key. Looks very similar to the sort of key that was onced used 
to access restricted levels in an elevator.""",
    
    "usable": False,
    
    "power": 0
}

item_beans = {
    "id": "beans",
    
    "name": "a tin of beans",

    "description":
    """An old tin of beans. Look very old but they were made before use-by dates 
so they must be edible""",
    
    "usable": True,
    
    "power": 0
}

item_medicine = {
    "id": "medicine",
    
    "name": "medicine",

    "description":
    """A small bottle of paracetamol, could be used to increase health by 
relieving pain or dropping a fever. Theres not nearly enough to cause 
    overdose...""",
    
    "usable": True,
    
    "power": 0
}

item_shoes = {
    "id": "shoes",
    
    "name": "an old pair of shoes",

    "description":
    """An old pair of shoes. They are a size to big and are quite damp but they 
will protect your feet from anything sharp on the floor.""",
    
    "usable": False,
    
    "power": 0
}

item_notepad = {
    "id": "notepad",
    
    "name": "a notepad",
    
    "description":
    """A small notepad and pen. It's blank and you could use it to make some notes.""",
    
    "usable": True,
    
    "power": 0,
    
    "content": ["Watch your step!"]
}

item_note1 = {
    "id": "note1",
    
    "name": "a note numbered " + str(note1),
    
    "description": "A burnt note. You can barely see the writing on it. '" + str(note1) + "'",
    
    "usable": False,
    
    "power": 0,
    
    "content": note1
}

item_note2 = {
    "id": "note2",
    
    "name": "a note numbered " + str(note2),
    
    "description": "A burnt note. You can barely see the writing on it. '" + str(note2) + "'",
    
    "usable": False,
    
    "power": 0,
    
    "content": note2
}

item_note3 = {
    "id": "note3",
    
    "name": "a note numbered " + str(note3),
    
    "description": "A burnt note. You can barely see the writing on it. '" + str(note3) + "'",
    
    "usable": False,
    
    "power": 0,
    
    "content": note3
}

item_note4 = {
    "id": "note4",
    
    "name": "a note numbered " + str(note4),
    
    "description": "A burnt note. You can barely see the writing on it. '" + str(note4) + "'",
    
    "usable": False,
    
    "power": 0,
    
    "content": note4
}

item_note5 = {
    "id": "note5",
    
    "name": "a note numbered " + str(note5),
    
    "description": "A burnt note. You can barely see the writing on it. '" + str(note5) + "'",
    
    "usable": False,
    
    "power": 0,
    
    "content": note5
}

item_note6 = {
    "id": "note6",
    
    "name": "a note numbered " + str(note6),
    
    "description": "A burnt note. You can barely see the writing on it. '" + str(note6) + "'",
    
    "usable": False,
    
    "power": 0,
    
    "content": note6
}

item_clue1 = {
    "id": "clue1",
    
    "name": "clue number 1",
    
    "description":
    """To whoever finds this,
The doctors in here are sick. They have us locked in this nightmare of a hospital
with no way of escaping. They use the door. A big metal door. But only they know
the code. I tried to take a peak at it once but that did not end well for me...
Still though, I remember it consisted of only 0s and 1s.
If only I had taken a better look...""",

    "usable": False,
    
    "power": 0
}

item_clue2 = {
    "id": "clue2",
    
    "name": "clue number 2",
    
    "description":
    """I hope whoever is reading this can make out my writing. I have tried for
weeks to escape this hellhole, but with no avail. I seem to recall the code 
system having some connection with sign & magnitude, but my mind is frail,
so perhaps you shouldn’t trust what I say...""",

    "usable": False,
    
    "power": 0
}

item_clue3 = {
    "id": "clue3",
    
    "name": "clue number 3",
    
    "description":
    """You can’t escape. You might as well give up. I’ve tried so many times.
If only I knew what two’s complement is? If to whom ever finds this note knows
anything about this bizarre method, by all means try an escape, not that your mind
will ever recover from the images seared into your retinas from this retched hospital.""",

    "usable": False,
    
    "power": 0
}

items = {
    "torch": item_torch,
    "axe": item_axe,
    "salt": item_salt,
    "bible": item_bible,
    "knife": item_knife,
    "water": item_water,
    "crucifix": item_crucifix,
    "key": item_key,
    "beans": item_beans,
    "medicine": item_medicine,
    "shoes": item_shoes,
    "notepad": item_notepad,
    "note1": item_note1,
    "note2": item_note2,
    "note3": item_note3,
    "note4": item_note4,
    "note5": item_note5,
    "note6": item_note6
}