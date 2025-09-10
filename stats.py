def get_num_words(text):
    character_list = text.split()
    return len(character_list)

def count_chars(text):
    character_count = {}
    for character in text.lower(): 
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1  
    return character_count

def sort_on(items):
    return items["num"]

def sorted_dictionaries(dictionary):
    sorted_dicts = []
    for character in dictionary:
        item = {"char":character, "num":dictionary[character]} 
        sorted_dicts.append(item)
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts

