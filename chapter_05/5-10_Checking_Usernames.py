current_users = ['admin', 'iloverugs', 'Sheffwang', 'bmerges', 'blmerges']
new_users = ['iloverugs', 'bmerges', 'bear1r0n', 'marriedkate', 'kipo']

current_users_lwr = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lwr:
        print(f"The username '{new_user}' has already been taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")