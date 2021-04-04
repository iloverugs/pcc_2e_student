country_rivers = {
    'nile': 'egypt',
    'usa': 'mississipi',
    'syria': 'euphrates',
    }

abbreviated_country = ['usa']

for country, river in country_rivers.items():
    if country in abbreviated_country:
        print(f"The {river.title()} runs through {country.upper()}.")
    else:
        print(f"The {river.title()} runs through {country.title()}.")

print()
for river in country_rivers.values():
    print(river.title())

print()
for country in country_rivers.keys():
    if country in abbreviated_country:
        print(country.upper())
    else:
        print(country.title())