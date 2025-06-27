def word_counter(text):
    words = text.split()
    return len(words)

def count_char(character):
    characters = character.lower()
    char_counts = {}
    for char in characters:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def cleaner(counts):
    character_list = []

    for char, count in counts.items():
        if char.isalpha():
            character_list.append({"char" : char, "num" : count })
    
    character_list.sort(reverse = True, key=lambda x: x["num"])

    return character_list

