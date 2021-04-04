rpg_played = ['zelda', 'Persona', 'Xenoblade', 'fallout series', 'elder scrolls', 'assassins creed']
print(rpg_played)
print(sorted(rpg_played))
print(sorted(rpg_played, reverse=True))
rpg_played.reverse()
print(rpg_played)
rpg_played.sort()
print(rpg_played)
rpg_played.append('Deus Ex')
print(rpg_played)
rpg_played.sort(reverse=True)
print(rpg_played)

dont_like = 'assassins creed'
rpg_played.remove(dont_like)
print(rpg_played)