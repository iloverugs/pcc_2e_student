filenames = [
        'metamorphosis.txt', 'dracula.txt',
        'heart_of_darkness.txt', 'alice.txt'
            ]
for filename in filenames:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
        number_of_the = contents.lower().count("the ")
        print(
            f"The file {filename} contains the word "
            f"'the' {number_of_the} number of times."
            )