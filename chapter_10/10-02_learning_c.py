# Read in each line from file, and replace 'Python' with 'Ruby'
file = 'learning_python.txt'

with open(file) as file_object:
    contents = file_object.read()
    contents_mod = contents.replace('Python', 'Ruby')
print(contents_mod)