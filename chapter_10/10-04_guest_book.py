# while loop prompts user for name
# print greeting to screen and add a line recording their visit in file
# Every entry appears on a new line in the file
filename = 'guest_book.txt'

while True:
    # prompt for name, q to quit
    guest_name = input("What is your name? Enter 'q' to quit. ")
    if guest_name == 'q':
        break
    else:
        # print greeting, append to filename on a new line
        print(f"Hello {guest_name}.")
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest_name}\n")
