# function make_shirt() accept size and text of a message printed on shirt
# summarize the size of shirt and message
def make_shirt(size, message):
    """print size and message of shirt"""
    print(f"\nThe size of the shirt is {size}.")
    print(f"The message on the shirt says: {message}")

make_shirt('medium', "What a cool shirt!")
make_shirt(size='large', message='The wearer is probably an average American')