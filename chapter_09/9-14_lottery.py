from random import choice

lottery_values = (
        '01', '13', '26', '38', '40', '52', '63', '79', '88', '96', 'a', 'b', 'f', 'j', 'k'
        )

lottery_win = []
while len(lottery_win) < 4:
    # Keep from using the same values twice
    pulled_value = choice(lottery_values)
    if pulled_value not in lottery_win:
        lottery_win.append(pulled_value)

print("Any ticket matching these four numbers or letters wins a prize!")
print(f"\t{lottery_win}")