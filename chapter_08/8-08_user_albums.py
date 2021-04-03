# function make_ablum() builds dictionary describing a music album
# optional parameter set to None, store number of songs on an album
def make_album(artist_name, album_title, song_count=None):
    """Return dictionary of information about an album."""
    if song_count:
        album_dict = {
        'artist': artist_name,
        'title': album_title,
        'number_of_songs': song_count,
        }
    else:
        album_dict = {'artist': artist_name, 'title': album_title}
    return album_dict

# while loop that allows users to enter album's artist and title
while True:
    print("Enter artist name, then album title.")
    print("Enter q to quit.")
    a_name = input("Artist/Band name: ").title()
    # if you use title, single letters get capitalized dammit
    if a_name.lower() == 'q':
        break
    a_title = input("Album Title: ").title()
    if a_title.lower() == 'q':
        break

    # Added optional song count for fun
    print("Optional: Enter number of songs?")
    count_option = input("Y or N: ")
    s_count=None
    if count_option.lower() == 'y':
        s_count = input("Number of songs (numbers only): ")
    elif count_option.lower() == 'q':
        break

    album_info = make_album(a_name, a_title, s_count)
    print(album_info)