dogs = ['Brittany', 'Poodle', 'German Shepard', 'Huskie']
my_dog = 'Brittany'
print("Is dog == 'Brittany'? I predict True.")
print(my_dog == 'Brittany')

print("\nIs dog == 'brittany'? I predict True.")
print(my_dog.lower() == 'brittany')

print("\nIf dogs == 'Brittany', print 'Rugger!'")
for dog in dogs:
    if dog == 'Brittany':
        print('My dog Rugger!')
    else:
        print(dog.lower())

print("\nIf dog =! 'Brittany', print 'My dog isnt a ___")
for dog in dogs:
    if dog != 'Brittany':
        print(f"My dog isn't a {dog.lower()}")
    else:
        print(f"My dog is a brittany!")

print("\nIs dog == 'Poodle'? I predict False.")
print(my_dog == 'Poodle')

print("\nIs Huskie in the list? I predict True")
if 'Huskie' in dogs:
    print(True)
else:
    print(False)

print("\nIs dalmation in the list? I predict False")
if 'dalmation' in dogs:
    print(True)
else:
    print(False)

num_0 = 13
num_1 = 45
num_2 = 89

if num_0 >= 1:
    print(True)
else:
    print(False)