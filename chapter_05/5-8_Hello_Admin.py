#usernames = ['admin', 'iloverugs', 'Sheffwang', 'bmerges', 'blmerges']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, you have complete access to this account.')
        else:
            print(f"Hello {username}, you have limited access to this account.")
else:
    print("We need to find some users!")