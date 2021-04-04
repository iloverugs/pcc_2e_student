favorite_numbers = {
    'bryan': [0, 12],
    'bruce': [16],
    'ben': [11_181_991],
    'jason': [6],
    'kate': [11, 18],
    'chris': [3],
    'aeja': [1],
    }

for name, num in favorite_numbers.items():
    if len(num) == 1:
        print(f"{name.title()}'s favorite number is:")
        for n in num:
            print(f"\t{n}")
    else:
        print(f"{name.title()}'s favorite numbers are:")
        for n in num:
            print(f"\t{n}")