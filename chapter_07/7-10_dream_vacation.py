# 7-10 Write program that polls users about their dream vacation
dream_vacations = []

polling_active = True

while polling_active:
    prompt = "\nWhere is your dream vacation spot?"
    dvp = input(prompt)

    dream_vacations.append(dvp)

    # Check for more pollers
    pollers = True
    while pollers:
        prompt = "Are there any more pollers? (Y/N) "
        poller = input(prompt).lower()

        if poller == "n":
            polling_active = False
            pollers = False
        elif poller == 'y':
            pollers = False
        else:
            print("Invalid input. Y or N only.")

# Count all spots, add {location : poll#} in dictionary.
dv_dict = {}
for dv in dream_vacations:
    if dv not in dv_dict:
        dv_dict[dv] = 1
    else:
        dv_dict[dv] += 1

#    dv_dict[dv] = dream_vacations.count(dv)

# dv_dict = {dv: dream_vacations.count(dv) for dv in dream_vacations}

print("These are the polls for vacation spots: ")
print(dv_dict)
