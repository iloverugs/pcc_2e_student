# Program reads file and prints what I wrote 3 times
file_name = 'learning_python.txt'

with open(file_name) as file_object:
    # Print contents of entire file
    contents = file_object.read()
print(contents)

with open(file_name) as file_object:
    # Print by looping over the file object
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    # Print by storing all lines in a list
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
