import random
import string
import json

def weighted_random():
    weights = {5: 5.0, 6: 20.0, 7: 50.0, 8: 20.0, 9: 5.0, 10: 1.0}
    length = random.choices(list(weights.keys()), weights=list(weights.values()))[0]
    print(length)  # Debugging output
    return length

def random_string():
    length = weighted_random()
    word = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    print(word)  # Debugging output
    return word

def load_dictionary():
    """Load dictionary from JSON file"""
    try:
        with open('dictionary_alpha_arrays.json', 'r') as f:
            dictionary_data = json.load(f)
        
        # If it's a list, merge all dictionaries into one
        if isinstance(dictionary_data, list):
            merged_dict = {}
            for dict_entry in dictionary_data:
                if isinstance(dict_entry, dict):
                    merged_dict.update(dict_entry)
            return merged_dict
        else:
            return dictionary_data
    except FileNotFoundError:
        print("Dictionary file not found!")
        return {}
    except Exception as e:
        print(f"Error loading dictionary: {e}")
        return {}

def word_check(word):
    """Check if a word exists in the dictionary and return its definition"""
    dictionary = load_dictionary()
    
    if not dictionary:
        return False
    
    # Check if the word exists in the dictionary (case-insensitive)
    word_lower = word.lower()
    
    if word_lower in dictionary:
        return dictionary[word_lower]
    
    # Also check the original case
    if word in dictionary:
        return dictionary[word]
    
    return False

count = 0
while True:
    count += 1
    status = word_check(random_string())
    print(status)
    if status is not False:
        print(f"Found word after {count} attempts!")
        print(status)
        break
    # elif count % 100 == 0:  # Only print every 10,000 attempts
    #     print(f"Attempts: {count}")
