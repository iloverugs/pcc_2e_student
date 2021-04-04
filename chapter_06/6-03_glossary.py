glossary = {
    'upper': 'converts all leters in string to uppercase',
    'title': 'converts first letter in string to uppercase',
    'lower': 'converts all letters in string to lowercase',
    'print': 'prints to screen',
    'variable': 'function to assign a value to letters, words, numbers, and anything of the mix',
    'set': 'a collection in which each item must be unique',
    'dictionary': 'a collection of keys and their values',
    'if': 'allows examining the current state of a program and respond appropriately',
    'list': 'stores a mutable collection of items',
    'tuples': 'stores a collection of immutable items',
    'slice': 'a specific group of items in a list',
    }

for key, value in glossary.items():
    print(f"The programming word '{key}' does this: {value}.")