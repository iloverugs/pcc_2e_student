favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

take_poll = ['bob', 'edward', 'katherine', 'pete', 'phil']



for name in favorite_languages.keys():
    if name in take_poll:
        print(f"{name.title()}, please take the poll.")
    else:
        print(f"{name.title()}, thank you for taking the poll.")

for pollster in take_poll:
    if pollster not in favorite_languages:
        print(f"{pollster.title()}, please take the poll.")