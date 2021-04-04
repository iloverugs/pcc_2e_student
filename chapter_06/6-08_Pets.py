# Make a list of pets, and each pet a dictionary about type of animal and owner's name
# NO ACTUALLY, make a list of pets, each a dictionary about the type and name of the animal and the owner's name.
pets = []

pet = {
    'animal': 'dog',
    'name': 'rugger',
    'owner': ['bryan'],
    }
pets.append(pet)      

pet = {
    'animal': 'cat',
    'name': 'kipo',
    'owner': ['kate', 'ben']
    }
pets.append(pet)

pet = {
    'animal': 'cat',
    'name': 'moose',
    'owner': ['Jason', 'Hallie'],
    }
pets.append(pet)
    
pet = {
    'animal': 'cat',
    'name': 'Rue',
    'owner': ['jason', 'hallie'],
    }
pets.append(pet)

for pet in pets:
    print(f"\nPet type: {pet['animal'].title()}")
    print(f"Pet name: {pet['name'].title()}")
    if len(pet['owner']) == 1:
        for o in pet['owner']:
            print(f"Pet owner: {o.title()}")
    else:
        print("Pet owners:")
        for o in pet['owner']:
            print(f"\t {o.title()}")
