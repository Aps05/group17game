#!/usr/bin/python3

import os.path
from map import rooms
from player import *
from items import *
from parser_input import *
from enemies import *

def load_current_room(file):
    """This function finds and reads the current_room from a file 'file' and
    stores it in player['current_room'].
    """
    # make this true if the CURRENT ROOM line is found
    found_room = False
    for line in file:
        # if the room if found the load it in current_room
        if found_room:
            player["current_room"] = rooms[line]
            break
        elif line == "CURRENT ROOM\n":
            found_room = True
            continue

def load_inventory(file):
    """This function reads all the inventory items that were stored in a file 'file'
    and stored them in the player's inventory.
    """
    #start with an empty inventory
    player["inventory"] = []
    
    found_inventory = False     
    for line in file:
        if found_inventory:
            if line == "\n":
                break
            line = line.strip("\n")
            player["inventory"].append(items[line])
        elif (line == "INVENTORY\n"):
            found_inventory = True
            continue

def load_rooms(file):
    """This function reads all the room items that were stored in a file 'file'
    and adds them to the corresponding room.
    """
    # global tells the function that it should use the "global"
    # current_room variable instead of create a new one that is
    # only vissible within this function
    global rooms
    found_rooms = False
    found_room = ""
    
    for line in file:
        if found_rooms:
            #end the loop when all rooms are loaded
            if line == "END ROOMS\n":
                found_rooms = False
                break
            #start loading each room's items
            line = line.strip("\n")
            if line == line.upper():
                #the method .title() capitalises the 1st letter
                #of each word in the string
                line = line.lower()
                found_room = line.title()
                continue
            elif (found_room != "") and (line != ""):
                rooms[found_room]["items"].append(items[line])
            else:
                found_room = ""
                continue
        elif (line == "ROOMS\n"):
            found_rooms = True
            continue

def empty_rooms():
    """This function emptys all the items from all the rooms.
    """
    global rooms
    for roomId,room in rooms.items():
        rooms[roomId]["items"] = []
        
def load_notepad(file):
    """This function finds the line labled 'NOTEPAD' in a file 'file' and stores
    all the following lines in the contents of item_notepad until it encounters an empty line.
    """
    global item_notepad
    # used to know when the content of the notepad is found
    found_notepad = False
    # empty the notepad to used saved content
    item_notepad["content"] = []
    
    for line in file:
        if found_notepad:
            if line != "\n":
                line = line.strip("\n")
                item_notepad["content"].append(line)
                continue
            break
        elif line == "NOTEPAD\n":
            # NOTEPAD title found so next line will will include notepad content
            found_notepad = True
            continue

def load_game():
    """This function loads all the information stored in save.txt to restore
    the game to the state where it was saved.
    """
    # check if a save file exists
    if not os.path.exists("save.txt"):
        print("You do not have a save file.")
    else:
        # open save.txt in read mode
        file = open("save.txt", 'r')
        #load inventory
        load_inventory(file)
        # emptry tooms of all items to add the items
        # that were storedin save.txt        
        empty_rooms()
        load_rooms(file)
        # load the notepad
        load_notepad(file)
        # load the room the player was in        
        load_current_room(file)
        #close the file
        file.close()
        
        print("Adventure Loaded")        

def save_game():
    """This function saves all the required information so that the game can be
    continued exactly from where it was left off. It stores data in save.txt
    """
    # Re-write the previous saved file
    file = open("save.txt", 'w')
    file = open("save.txt", 'r+')

    
    # Save inventory
    file.write("INVENTORY\n")
    for item in player["inventory"]:
        file.write("%s\n" % item["id"])
    file.write("\n")
    
    # Save room items
    file.write("ROOMS\n")
    for roomId,room in rooms.items():        
        file.write(roomId.upper())
        file.write("\n")
        for item in room["items"]:
            file.write(item["id"])
            file.write("\n")
    file.write("END ROOMS\n\n")
    
    # Save the contents of the notepad
    file.write("NOTEPAD\n")
    for line in item_notepad["content"]:
        file.write("%s\n" % line) 
    file.write("\n")
    
    # Save current room
    file.write("CURRENT ROOM\n")
    file.write(player["current_room"]["id"])
    
    #close and save
    file.close()
    
    print("Adventure Saved")

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """
    if items == []:
        return 'no items'
    
    str_items = items[0]["name"]
    skip = False
    for item in items:
        if skip:
            str_items += ", " + item["name"]
        else:
            skip=True
        
    return str_items

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names.
    """
    if room["items"] != []:
        item_list = list_of_items(room["items"])
        string = "There is " + item_list + " here."
        print(string)
        print()

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here."
    """
    item_list = list_of_items(items)
    item_list = "You have " + item_list + "."
    print(item_list)
    print()

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this).
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    if room["items"] != []:
        print_room_items(room)
        #print()

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads.
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line.
    """
    
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    """
    
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    # Print any items in the room
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    # Print any items in the player's inventory
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["id"] + ".")
    # Print any items in player's inventory that are usable
    for item in inv_items:
        if item["usable"]:
            print("USE " + item["id"].upper() + " to use your " + item["id"] + ".")
    # I realise that the "DROP" and "USE" loop can be combined into one loop
    # but I want all the drop items to be printed 1st and then all the usable items
    print("INSPECT any of your items.")
    print("Go to main MENU.")
    
    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    """
    return chosen_exit in exits
    
def write_notepad():
    """This function gets a string from the player and wirtes it in the notepad
    """
    # Write to notepad
    string = input("Write > ")
    
    if string == "":
        return
    item_notepad["content"].append(string)
    
    return

def erase_notepad():
    """This function gets a line from the user and erases it from the notepad
    """
    line_number = int(input("Which line do you want to erase? "))
    while line_number < 0:
        print("You can't have a negative line number...")
        line_number = int(input("Which line do you want to erase? "))
    # used to count the lines in notepad    
    n = 0
    while line_number >= n:
        n = 0
        for line in item_notepad["content"]:
            if line_number == n:
                item_notepad["content"].remove(line)
                n += 1
                break
            else:
                n += 1
                
    return
    
def display_notepad():
    """This function displays everything that the player wrote in his notepad
    and allows him to write something new. 
    """
    print("NOTEPAD:\n")
    # used to enumerate lines
    n = 0
    for lines in item_notepad["content"]:
        print(str(n) + ". " + lines)
        n += 1
    print()    
    return
    
def print_notepad_menu():
    """This function prints the notepad menu and receives an input from the user
    """
    while True:
        display_notepad()
        print("NOTEPAD MENU:\n")
        print("Write to notepad.")
        print("Erase from notepad.")
        print("Close notepad.")
        print("What do you want to do?\n")
    
        user_input = input("> ")
        user_input = normalise_input(user_input, True)
        
        if user_input == []:
            print("That's not a valid command.")
        elif user_input[0] == "view":
            display_notepad()
        elif user_input[0] == "write":
            write_notepad()
        elif user_input[0] == "erase":
            erase_notepad()
        elif user_input[0] == "close":
            return
        else:
            print("That's not a valid command.")

def execute_go(direction, room):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    
    global player
    if direction in room["exits"]:
        player["current_room"] = rooms[room["exits"][direction]]
    else:
        print("You can't go that way.")
        print()


def execute_take(item_id, room):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    if item_id not in items:
        print("This item doesn't exist.")
    elif items[item_id] not in room["items"]:
        print("You don't see " + items[item_id]["name"])
    else:
        player["inventory"].append(items[item_id])
        room["items"].remove(items[item_id])
        print("You took",items[item_id]["name"])
        return
            
def execute_drop(item_id, room):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    if item_id not in items:
        print("There is no such item.")
    elif items[item_id] not in player["inventory"]:
        print("You don't have " + items[item_id]["name"])
    else:
        player["inventory"].remove(items[item_id])
        room["items"].append(items[item_id])
        print("You dropped ",items[item_id]["name"])
        return

def execute_use(item_id):
    if items[item_id] in player["inventory"]:
        if item_id == "notepad":    
            print_notepad_menu()
    else:
        print("You do not have " + items[item_id]["name"])
        
def execute_inspect(item_id):
    if item_id in items:
        if items[item_id] in player["inventory"]:
            print(items[item_id]["description"])
        else:
            print("You don't have " + items[item_id]["name"])
    else:
        print("This ites doesn't exist.")
        
def execute_command(command, room):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1], room)
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1], room)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1], room)
        else:
            print("Drop what?")
            
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")
    elif command[0] == "menu":
        return "menu"
        
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
            
    elif (command[0] == "quit") or (command[0] == "exit"):
        return "Quit"
    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
    print()
    
    # Normalise the input
    normalised_user_input = normalise_input(user_input, False)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    """

    # Next room to go to
    return rooms[exits[direction]]

def main_menu(game_started):
    # Print main menu
    print("MAIN MENU:\n")
    # If game has started print continue. Else print new game.
    if not game_started:
        print("New Game")
    else:
        print("Continue Game")
    print("Load Game\nSave Game\nQuit Game")
    #Get input from user
    choice = str(input("> Chose Option: "))
    print()
    #make all letters lower case
    choice = choice.lower()
    
    if (choice == "new game") or (choice == "new"):
        return ""
    if (choice == "continue game") or (choice == "continue"):
        return ""
    elif (choice == "load game") or (choice == "load"):
        load_game()
        return ""
    elif (choice == "save game") or (choice == "save"):
        save_game()
    elif (choice == "quit game") or (choice == "quit"):
        return "Quit"

# This is the entry point of our program
def main():
    game_started = False
    # Print main menu and heck if player wants to quit
    menu_option = main_menu(game_started)
    
    # Main game loop
    # If player wants to quit don't enter loop
    while menu_option != "Quit":
        game_started = True
        # Display game status (room description, inventory etc.)
        print_room(player["current_room"])
        print_inventory_items(player["inventory"])

        # Show the menu with possible actions and ask the player
        command = menu(player["current_room"]["exits"], player["current_room"]["items"], player["inventory"])

        # Execute the player's command
        menu_option = execute_command(command, player["current_room"])
        # If player asks for main menu, display main menu
        if menu_option == "menu":
            menu_option = main_menu(game_started)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
    #save_game()
    #load_game()