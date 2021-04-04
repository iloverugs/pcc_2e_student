# Prompt for the user's favorite number
# Store with json.dump() in a file.
# Another program reads value in file and prints message
import json

filename = "favorite_numbers.json"


def prompt_fav_number():
    """Prompt for the user's favorite number. Store in file."""
    fav_nbr = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(fav_nbr, f)
    return fav_nbr

def read_fav_number():
    """Get stored number if available."""
    try:
        with open(filename) as f:
            fav_nbr = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_nbr

def print_fav_number(fav_nbr):
    """Prints favorite number in a message."""
    print(f"I know your favorite number! It's {fav_nbr}.")

def favorite_number():
    """Prints user's favorite number in a message."""
    fav_nbr = read_fav_number()
    if fav_nbr:
        print_fav_number(fav_nbr)
    else:
        fav_nbr = prompt_fav_number()
        print_fav_number(fav_nbr)

favorite_number()