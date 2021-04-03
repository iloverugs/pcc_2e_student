# The ' * ' tells Python to make an empty tuple of Parameter
# And pack whatever values it recieves into this tuple
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepproni')
make_pizza("mushrooms", 'green peppers', 'extra cheese')

