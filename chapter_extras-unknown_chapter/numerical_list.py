numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


odd_numbers = []
for value in range(0, 20, 2):
	odd_number = value + 1
	odd_numbers.append(odd_number)

print(odd_numbers)

multiples_3 = []
for value in range(1, 11):
	multiple_3 = value * 3
	multiples_3.append(multiple_3)

print(multiples_3)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
