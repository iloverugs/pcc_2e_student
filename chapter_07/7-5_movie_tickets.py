customer = 'y'

while customer.lower() == 'y':
    prompt = "\nWelcome to the theater!"
    prompt += "\nPlease enter your age: "

    age = int(input(prompt))

    if age < 3:
        cost = '$0'
    elif age < 13
        cost = '$10'
    else:
        cost = '$15'

    print(f"\nThe price of admission is {cost}.")

    prompt = "Are there any other customers? Y or N "
    customer = input(prompt)
