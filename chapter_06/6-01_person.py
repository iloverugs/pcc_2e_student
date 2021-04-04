personal_info = {
    'first name': 'aeja',
    'last name': 'merges',
    'year of birth': 1963,
    'month of birth': 9,
    'day of birth': 28,
    'country of residence': 'usa',
    'state of residence': 'nh',
    'city of residence': 'bow',
    'zip code': '03304',
    }

fname = personal_info['first name'].title()
lname = personal_info['last name'].title()
mob = personal_info['month of birth']
dob = personal_info['day of birth']
yob = personal_info['year of birth']
country_residence = personal_info['country of residence'].upper()
state_residence = personal_info['state of residence'].title()
city_residence = personal_info['city of residence'].title()
z_code = personal_info['zip code']

print(f"Name: {fname} {lname}")
print(f"Date of birth: {mob}/{dob}/{yob}")
print(f"Current Residence: {city_residence}, {state_residence}, {z_code} {country_residence}")