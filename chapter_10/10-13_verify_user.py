import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def verify_user(username):
    """Verify if the current user used this program last."""
    verified = input(f"Are you {username}? Enter 'y' or 'n': ").lower()
    if verified == 'n':
        return False
    else:
        return True

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        if verify_user(username):
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        
greet_user()