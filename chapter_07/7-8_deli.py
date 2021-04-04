# Make a list called sandwich_orders and fill it with
# with the names of various sandwiches.
sandwich_orders = ['rueben', 'ham and cheese',
    'turkey', 'peanut butter and jelly',]
# Empty list of finished_sandwiches.
finished_sandwiches = []

while sandwich_orders:
    # move sandwich_order to finished_sandwiches.
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)

    # print finished_sandwich in sentence.
    print(f"Making a {finished_sandwich} sandwich.")

#print list of finished_sandwiches
print("\nThese are the sandwiches ordered: ")
print(finished_sandwiches)