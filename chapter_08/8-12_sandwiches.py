# Function accepts list of items person wants on a sandwich
def sandwich(bread_type, stacks, *ingrediants):
    """Function prints summary of sandwich ordered"""
    print(f"Making a {stacks}-stack {bread_type}-bread "
        "sandwich with the following ingrediants: ")
    for ingrediant in ingrediants:
        print(f"- {ingrediant}")

# Call function 3 times, using different number of arguments each time
sandwich1 = sandwich('wheat', 'double', 'ham', 'cheese', 'tomato', 'lettuce', 'pickles')
sandwich2 = sandwich("white", 'single', 'peanut butter', 'jam')
sandwich3 = sandwich('rye', 'triple', 'turkey breast', 'provolone cheese', 'pickles')
