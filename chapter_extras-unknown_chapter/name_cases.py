#first project, print a name as a variable in a message
name = "bryan"

message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

print(name.lower())
print(name.upper())

#print a quote from a famous person, quoting that person in the message
quote = "You may be disappointed if you fail, but you are doomed if you don't try."
famous_person = "beverly sills"

message = f'{famous_person.title()} is known to have said, "{quote}"'
print(message)

#print a name with extra whitespace, add \n and \t functions.
#use rstrip, lstrip and strip to get rid of whitespace
name = " Steve Rogers\n\tPseudonym:\n\t\tCaptain America  "
print(name.strip())