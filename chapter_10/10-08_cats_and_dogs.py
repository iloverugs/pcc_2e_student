# Open file, print contents. If not found, print error exception.
filenames = ["cats.txt", 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # 10-09: make error exception silent
        pass
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        print(contents.rstrip())

