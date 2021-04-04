personal_info = {
    'amerges' : {
        'first name': 'aeja',
        'last name': 'merges',
        'year of birth': 1963,
        'month of birth': 9,
        'day of birth': 28,
        'country of residence': 'usa',
        'state of residence': 'nh',
        'city of residence': 'bow',
        'zip code': '03304',
        },

    'fbmerges' : {
        'first name': 'bruce',
        'last name': 'merges',
        'year of birth': 1957,
        'month of birth': 5,
        'day of birth': 16,
        'country of residence': 'usa',
        'state of residence': 'nh',
        'city of residence': 'bow',
        'zip code': '03304',
        },

    'fjmerges' : {
        'first name': 'jason',
        'last name': 'merges',
        'year of birth': 1988,
        'month of birth': 12,
        'day of birth': 30,
        'country of residence': 'usa',
        'state of residence': 'wa',
        'city of residence': 'seattle',
        'zip code': '98118',
        },

    }

for contact, contact_info in personal_info.items():
    print (f"\nContact: {contact}")
    full_name = f"{contact_info['first name']} "\
        f"{contact_info['last name']}"
    dob = f"{contact_info['month of birth']}/" \
        f"{contact_info['day of birth']}/" \
        f"{contact_info['year of birth']}"
    residence = f"{contact_info['city of residence']}, " \
        f"\n{contact_info['state of residence']}, " \
        f"\n{contact_info['country of residence']} " \
        f"{contact_info['zip code']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tYear of Birth: {dob}")
    print(f"\tResidence: {residence.title()}")






