# Wrap code in a while loop so the user can continue entering numbers
def addition_check():
    """
    Prompt two inputs, add together together and print answer.
    If ValueError, print friendly error msg.
    """
    while True:
        print("Enter two numbers to add them together. Input 'q' to quit.")
        var1 = input("First number: ")
        if var1 == 'q':
            break
        var2 = input("Second number: ")
        if var2 == 'q':
            break
        try:
            answer = (int(var1) + int(var2))
            print(f"{var1} + {var2} = {answer}")
        except ValueError:
            print("Input must be a number.")


addition_check()