# Make a list called sandwich_orders and fill it with
# with the names of various sandwiches.
# 7-9: add pastrami three times
sandwich_orders = [
    'rueben', 'pastrami', 'ham and cheese', 'pastrami',
    'turkey', 'peanut butter and jelly', 'pastrami',
    ]

# Empty list of finished_sandwiches.
finished_sandwiches = []

# 7-8 print deli has run out of pastrami
print("The deli has run out of pastrami.\n")

while sandwich_orders:
    # move sandwich_order to finished_sandwiches.
    #7-8 out of pastrami, remove all pastrami
    finished_sandwich = sandwich_orders.pop()
    if finished_sandwich != 'pastrami':
        finished_sandwiches.append(finished_sandwich)

        # print finished_sandwich in sentence.
        print(f"Making a {finished_sandwich} sandwich.")

#print list of finished_sandwiches
print("\nThese are the sandwiches finished: ")
print(finished_sandwiches)