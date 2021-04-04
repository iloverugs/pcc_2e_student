num = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
num = int(num)

if num % 10 == 0:
    print(f"\nThe number {num} is a multiple of ten.")
else:
    print(f"\nThe number {num} is not a multiple of ten.")