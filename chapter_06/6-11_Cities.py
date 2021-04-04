cities = {
    'seoul': {
        'country': 'south korea',
        'population': 9_967_677,
        'fact': '4th largest metropolitan economy',
            },
    'new york': {
        'country': 'united states of america',
        'population': 8_230_290,
        'fact': 'more than 800 languages spoken there',
        },
    'paris': {
        'country': 'france',
        'population': 11_078_546,
        'fact': 'known as the city of lights',
        }
    }

for city, facts in cities.items():
    print(f"\n{city.title()}:")
    for k, v in facts.items():
        if type(v) == int or type(v) == float:
            print(f"\t{k.title()}: {v}")
        else:
            print(f"\t{k.title()}: {v.title()}")
