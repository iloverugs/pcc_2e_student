def get_city_country(city, country, population=''):
    """Generates neatly formated string: 'city, country'."""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()