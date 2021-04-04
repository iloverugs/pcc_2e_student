prompt = "\nTell me what toppings you want for your pizza. Maximum of 10 toppings."
prompt = "\nEnter 'quit' when you are done. "

toppings = []

while True:
    topping = input(prompt)

    if (topping == 'quit') or len(toppings) == 10:
        print("These are you're selected toppings:")
        print(toppings)
        break
    else:
        toppings.append(topping)
        print(f"\nYou have selected {topping} as your topping.")

