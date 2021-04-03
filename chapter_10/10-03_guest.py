# Prompt user for their name. Write name to file guest.txt
filename = "guest.txt"

guest_name = input("What is your name? ")
with open(filename, 'w') as file_object:
    file_object.write(guest_name)