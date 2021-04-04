age = 33

if age < 2:
    stageoflife = ' baby'
elif age < 4:
    stageoflife = ' toddler'
elif age < 13:
    stageoflife = ' kid'
elif age < 20:
    stageoflife = ' teenager'
elif age < 65:
    stageoflife = 'n adult'
else:
    stageoflife = 'n elder'

print(f"The person is a{stageoflife}.")