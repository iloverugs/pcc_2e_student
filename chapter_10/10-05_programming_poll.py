# While loop asks people why they like programming
# Every answer, add reason to a file that stores all responses.
file_name = 'programming_poll.txt'

while True:
    reason = input("Why do you like programming? Input 'q' to quit. ")
    if reason == 'q':
        break
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(f"{reason}\n")