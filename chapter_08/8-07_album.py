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

# Make three dictionaries representing different albums with function
album = make_album('jimi hendrix', 'electric ladyland')
print(album)
album = make_album('the beatles', 'abbey road')
print(album)
ablum = make_album('bob dylan', 'rough and rowdy ways')
print(album)

# Make a function call that includes the number of songs on an ablum
album = make_album('amelia meath', 'sylvan eso', song_count=10)
print(album)