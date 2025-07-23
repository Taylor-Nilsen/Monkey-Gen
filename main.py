import random
import string
import json
import time

# Pre-compute everything for maximum speed
ASCII_LETTERS = string.ascii_letters
ASCII_LEN = len(ASCII_LETTERS)

# Convert to tuples for slightly faster access
WEIGHTS_KEYS = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)
WEIGHTS_VALUES = (0.09, 0.12, 0.13, 0.18, 0.25, 0.36, 0.63, 1.09, 2.07, 3.82, 10.10, 20.00, 37.04, 45.45, 90.91, 166.67, 200.00, 500.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00)

# Pre-import functions for faster access
random_choices = random.choices
random_choice = random.choice
time_time = time.time

start_time = time_time()

def random_string_optimized():
    # Use pre-computed lists - faster than dict lookups
    length = random.choices(WEIGHTS_KEYS, weights=WEIGHTS_VALUES)[0]
    # Use random.choices with k parameter - faster than loop
    return ''.join(random.choices(ASCII_LETTERS, k=length))

# Load dictionary once at startup
print("Loading dictionary...")
DICTIONARY = {}
try:
    with open('dictionary_alpha_arrays.json', 'r') as f:
        dictionary_data = json.load(f)
    
    if isinstance(dictionary_data, list):
        for dict_entry in dictionary_data:
            if isinstance(dict_entry, dict):
                DICTIONARY.update(dict_entry)
    else:
        DICTIONARY = dictionary_data
    print(f"Dictionary loaded: {len(DICTIONARY)} words")
except FileNotFoundError:
    print("Dictionary file not found!")
except Exception as e:
    print(f"Error loading dictionary: {e}")

# Create a set for O(1) word existence checking
WORD_SET = set(DICTIONARY.keys())

def word_check_fast(word):
    # Fast existence check first
    if word in WORD_SET:
        return f"\n\033[1m{word}\033[0m: \n{DICTIONARY[word]}"
    return False

count = 0
print("Starting simple optimized single-threaded search...")

# Simple fast loop - no complex batching
while True:
    count += 1
    
    # Inline optimized generation for speed
    length = random.choices(WEIGHTS_KEYS, weights=WEIGHTS_VALUES)[0]
    word = ''.join(random.choices(ASCII_LETTERS, k=length))
    
    # Fast word check
    if word in WORD_SET:
        elapsed_time = time.time() - start_time
        print(f"Found word after {count:,} attempts in {elapsed_time:.1f} seconds!")
        print(f"Speed: {count / elapsed_time:,.0f} attempts/sec")
        print(f"\n\033[1m{word}\033[0m: \n{DICTIONARY[word]}")
        break
    
    # Progress report every 50k attempts
    if count % 50000 == 0:
        elapsed_time = time.time() - start_time
        speed = count / elapsed_time if elapsed_time > 0 else 0
        print(f"Attempts: {count:,}, Speed: {speed:,.0f} attempts/sec")