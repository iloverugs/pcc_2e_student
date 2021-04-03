# The ' * ' tells Python to make an empty tuple of Parameter
# And pack whatever values it recieves into this tuple

# *function must be placed last in the function definition
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepproni')
make_pizza(12, "mushrooms", 'green peppers', 'extra cheese')

# generally ' *args ' is used as a parameter name