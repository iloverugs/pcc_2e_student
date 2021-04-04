# Prompt for two numbers. Add together and print result.
# Catch ValueError if either input not a number, and print friendly error msg.
def addition_check():
    """
    Prompt two inputs, add together and print answer.
    If ValueError, print friendly error msg.
    """
    var1 = input("Enter two numbers. First number: ")
    var2 = input("Second number: ")
    try:
        answer = (int(var1) + int(var2))
        print(f"{var1} + {var2} = {answer}")
    except ValueError:
        print("Input must be a number.")


addition_check()