#Define function with parameters
def describe_pet(animal_type, pet_name):
    """Display information about a pet,"""
    print(f"\nI have a {animal_type.lower()}.")
    print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")

#call function with positional arguments
describe_pet('Cat', 'kipo')
describe_pet('dog', 'bernie')

#call function with keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

