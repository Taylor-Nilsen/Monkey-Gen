# Monkey Gen

A Python-based random word generator that creates random letter combinations and validates them against a comprehensive English dictionary. The generator uses a bell-curve distribution for word lengths and performs real-time dictionary validation.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![JSON](https://img.shields.io/badge/Dictionary-102K_Words-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## Features

- **Intelligent word generation**: Creates random strings with statistically realistic length distributions
- **Bell-curve length weighting**: 7-letter words are most common, with decreasing probability for shorter/longer words
- **Comprehensive dictionary validation**: Validates against 102,000+ English words from merged dictionary sources
- **Real-time word discovery**: Continuously generates and tests random combinations until a valid word is found
- **Low-overhead status tracking**: Efficient progress monitoring with minimal performance impact
- **Case-insensitive matching**: Finds words regardless of capitalization
- **Complete definitions**: Returns full dictionary definitions for discovered words

## Quick Start

### Prerequisites

- Python 3.6 or higher
- `dictionary_alpha_arrays.json` file (included in repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Taylor-Nilsen/Monkey-Gen.git
   cd Monkey-Gen
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

## How It Works

The Monkey Gen algorithm operates on the principle of infinite monkey theorem - given enough time, random letter combinations will eventually produce valid words.

### Process Flow

1. **Length Generation**: Uses weighted random selection with bell-curve distribution centered on 7 letters
2. **Character Selection**: Randomly selects letters from the English alphabet (a-z, A-Z)
3. **Dictionary Validation**: Checks generated string against comprehensive word database
4. **Definition Retrieval**: Returns complete dictionary definition when valid word is found
5. **Progress Tracking**: Counts attempts and provides periodic status updates

### Length Distribution

The generator uses a sophisticated weighted probability distribution for word lengths ranging from 5-27 characters:

- **Short words (5-7)**: Lower probability, easier to find
- **Medium words (8-12)**: Moderate probability, balanced discovery rate
- **Long words (13-20)**: Higher probability weights, more challenging to discover
- **Very long words (21-27)**: Maximum probability weights, extremely rare discoveries

The distribution is designed to balance discovery likelihood with word complexity, providing both quick wins with shorter words and exciting rare discoveries with longer words.

## Technical Details

**Dictionary Size**: 102,104 unique English words with complete definitions

**Dictionary Source**: Merged from 26 separate dictionary arrays containing historical and contemporary English vocabulary

**Word Length Range**: 5-27 characters with sophisticated weighted probability distribution

**Performance Optimizations**: 
- Pre-computed constants and tuples for maximum speed
- Inline word generation in main loop
- O(1) dictionary lookups using sets
- Minimal function call overhead
- Optimized random generation with `random.choices()`

**Memory Management**: Dictionary loaded once at startup and reused for all lookups

**Speed Tracking**: Real-time attempts-per-second monitoring and reporting

## Project Structure

```
Monkey-Gen/
├── main.py                      # Main application with optimized word generation logic
├── dictionary_alpha_arrays.json # Comprehensive English dictionary (102K+ words)
├── test.py                     # Alternative dictionary testing (WordNet integration)
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

### File Descriptions

- **main.py**: Highly optimized single-threaded word generator with performance tracking
- **dictionary_alpha_arrays.json**: Primary dictionary source with 102,104 words and definitions
- **test.py**: Experimental WordNet integration for alternative dictionary lookups
- **README.md**: Complete project documentation and usage guide

## Example Output

```
Loading dictionary...
Dictionary loaded: 102,104 words
Starting simple optimized single-threaded search...
Attempts: 50,000, Speed: 125,347 attempts/sec
Attempts: 100,000, Speed: 127,891 attempts/sec
Found word after 134,782 attempts in 1.1 seconds!
Speed: 122,529 attempts/sec

anarchic: 
Pertaining to anarchy; without rule or government; in political 
confusion; tending to produce anarchy; as, anarchic despotism; anarchical opinions.
```

## Functions

### `random_string_optimized()`
Generates random letter combinations using pre-computed weights and optimized character selection. Uses `random.choices()` for both length selection and character generation for maximum performance.

### `load_dictionary()`
Loads and merges all dictionary arrays from JSON file into a single searchable dictionary at startup. Creates both a dictionary for definitions and a set for O(1) existence checking.

### `word_check_fast(word)`
Performs ultra-fast word validation using set membership testing, then retrieves definition from dictionary if word exists.

## Performance Characteristics

- **Dictionary Loading**: One-time startup cost (~1-2 seconds)
- **Word Generation**: Highly optimized with pre-computed constants
- **Dictionary Lookup**: O(1) set membership testing + dictionary access
- **Average Speed**: 100,000+ attempts per second on modern hardware
- **Progress Reporting**: Every 50,000 attempts with speed tracking
- **Average Discovery Time**: Varies widely (seconds to hours depending on luck and word length)

## Customization

### Adjusting Length Distribution

Modify the `WEIGHTS_KEYS` and `WEIGHTS_VALUES` tuples to change length probabilities. The current distribution favors longer words for more exciting discoveries:

```python
# Current optimized weights (5-27 character range)
WEIGHTS_KEYS = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)
WEIGHTS_VALUES = (0.09, 0.12, 0.13, 0.18, 0.25, 0.36, 0.63, 1.09, 2.07, 3.82, 10.10, 20.00, 37.04, 45.45, 90.91, 166.67, 200.00, 500.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00)
```

### Progress Update Frequency

Change the modulo value to adjust status update frequency:

```python
if count % 50000 == 0:  # Print every 50,000 attempts (current)
```

## License

This project is open source and available under the MIT License.

## Troubleshooting

**Dictionary file not found?**
- Ensure `dictionary_alpha_arrays.json` is in the same directory as `main.py`
- Check file permissions and verify the JSON file is not corrupted

**Memory issues?**
- The dictionary requires ~50-100MB of RAM when loaded
- Close other memory-intensive applications if needed

**Slow performance?**
- Dictionary loading happens once at startup - subsequent lookups are extremely fast
- Modern hardware should achieve 100,000+ attempts per second
- Ensure no other CPU-intensive processes are running

**No words found?**
- The algorithm is probabilistic - some runs may take much longer than others
- Let it run longer, or restart for a fresh attempt with different random seed

## Contributing

Contributions are welcome! Areas for improvement:
- Additional dictionary sources
- Alternative generation algorithms  
- Further performance optimizations
- Statistical analysis tools
- GUI interface
- Multi-language dictionary support

