pizzas = ['cheese', 'sausage and mushroom', 'veggie', 'kimchi', 'peperoni']
for pizza in pizzas:
	print(f"{pizza.title()} is a good tasting pizza.")

print(f"I generally don't like pizza, but every now and then pizza is pretty good.\n")

animals = ['dog', 'wolf', 'coyote']
for canid in animals:
	print(f"{canid.title()} is an animal of the canid species.")

print("Canines, such as listed above, are a subspecies of the canid family.\n")

print("The first three pizzas in the list are:")
for pizza in pizzas[:3]:
	print(pizza)

print("\nThree pizzas from the middle of the list are:")
for pizza in pizzas[1:4]:
	print(pizza)

print("\nThe last three items in the list are:")
for pizza in pizzas[-3:]:
	print(pizza)

friend_pizzas = pizzas[:]
pizzas.append("spinach")
friend_pizzas.append("anchovy")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = ['pizza', 'falafel', 'carrot cake','ice cream']
print("\nMy friend and I like almost everything the same, except the last thing on both our lists.")
print("I like:")
for my_food in my_foods[-1:]:
	print(my_food)
print("But they like:")
for friend_food in friend_foods[-1:]:
	print(friend_food)