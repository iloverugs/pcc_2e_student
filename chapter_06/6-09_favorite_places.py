favorite_places = {
    'bryan': ['peru', 'frye island', 'jackson hole'],
    'aeja': ['new york', 'seoul'],
    'bruce': ['frye island', 'nepal'],
    }

for person, fplaces in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for fplace in fplaces:
        print(f"\t{fplace.title()}")
