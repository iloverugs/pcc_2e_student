guest_list = [ 'Rugger', 'Sadie', 'Kipo' ]
print(f"Please join me for dinner, {guest_list[0].title()}.")
print(f"Please join me for dinner, {guest_list[1].title()}.")
print(f"Please join me for dinner, {guest_list[2].title()}.")

cant_join = 'Sadie'
guest_list.remove(cant_join)
replacement = 'Poobear'
guest_list.append(replacement)

print(f"\nUnfortunately, {cant_join.title()} cannot make it.")

print(f"Please join me for dinner, {guest_list[0].title()}.")
print(f"Please join me for dinner, {guest_list[1].title()}.")
print(f"Please join me for dinner, {guest_list[2].title()}.")

guest_list.insert(0, 'Bob')
guest_list.insert(2, 'pete')
guest_list.append('Josh')
print('\nI have found a larger table everyone! Three more people can join!')
print(f"Please join me for dinner, {guest_list[0].title()}.")
print(f"Please join me for dinner, {guest_list[1].title()}.")
print(f"Please join me for dinner, {guest_list[2].title()}.")
print(f"Please join me for dinner, {guest_list[3].title()}.")
print(f"Please join me for dinner, {guest_list[4].title()}.")
print(f"Please join me for dinner, {guest_list[5].title()}.")

number_guest = len(guest_list)
print(f'That is {number_guest} people joining us for dinner.')

print('\nWhoops, made a mistake.  The table will not arrive in time. I only have space for two guests.')

cut_guest = guest_list.pop()
print(f'Sorry, {cut_guest.title()}, you are cut from my list.')
cut_guest = guest_list.pop()
print(f'Sorry, {cut_guest.title()}, you are cut from my list.')
cut_guest = guest_list.pop()
print(f'Sorry, {cut_guest.title()}, you are cut from my list.')
cut_guest = guest_list.pop()
print(f'Sorry, {cut_guest.title()}, you are cut from my list.')
print(f"Please join me for dinner, {guest_list[0].title()}.")
print(f"Please join me for dinner, {guest_list[1].title()}.")

del guest_list[0]
del guest_list[0]
print(guest_list)