# Modify make_shirt(), default size=large, message= "I love Python"
def make_shirt(size= 'large', message= "I love Python"):
    """print size and message of shirt"""
    print(f"\nThe size of the shirt is {size}.")
    print(f"The message on the shirt says: {message}")

# make large and medium shrit with default message
make_shirt()
make_shirt('medium')

# make shirt with different message
make_shirt('small', message="I'm frustrated by Python")