import string

# List of "valid" words (the rest are discarded)
valid_for_menu = ['north', 'east', 'south', 'west', 'go', 'take', 'drop',
               'knife', 'torch', 'axe', 'salt', 'bible', 'water', 'crucifix',
               'quit', 'exit', 'menu', 'up', 'down', 'key', 'beans', 'medicine',
               'shoes', 'notepad', 'use', 'inspect', 'look', 'note1', 'note2',
               'note3', 'note4', 'note5', 'note6', 'clue1', 'clue2', 'clue3', 'letter']
               
valid_for_notepad = ['write', 'erase','close', 'view']

valid_for_prepareEngage = ['engage', 'back']

valid_for_engage = ['attack', 'dodge', 'jump', 'run', 'escape', 'fist', 'fists',
                    'axe', 'knife', 'land']
                
valid_weapons = ['fists', 'fist', 'knife', 'axe']

def filter_words(words, valid_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    """
    
    new_words = []
    for word in words:
        if word in valid_words:
            new_words.append(word)

    return new_words
    
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:
    """
    
    no_punct = ""
    for char in text:
        if char == "'":
            no_punct += " "
            continue
        if not (char in string.punctuation):
            no_punct += char

    return no_punct


def normalise_input(user_input, valid_words):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:
    """
    
    # Remove punctuation and convert to lower case
    user_input = user_input.strip()
    no_punct = remove_punct(user_input).lower()
    filtered = filter_words(no_punct.split(), valid_words)
    
    return filtered