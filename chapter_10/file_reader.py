# open() function opens file as argument
# 'with' keyword closes file once access to it is no longer needed
# common convention to replace file location with variable
file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # rstrip rids extra lines
    # strip rids extra whitespace
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")