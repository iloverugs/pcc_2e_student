filename = 'programming.txt'

# open(file, 'w') creates/overwrites file
# open(file, 'a') appends to file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")