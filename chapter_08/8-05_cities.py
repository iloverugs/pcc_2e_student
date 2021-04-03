# Write function describe_city() accept city, country
# Give parameter default value
def describe_city(city, country="South Korea"):
    """display city in a country"""
    print(f"{city.title()} is in {country}")

describe_city('Seoul')
describe_city('Sunwon')
describe_city('Busan')