from random import choice


def winning_ticket(lottery_values):
    """Print a random collection of numbers from list as a winning ticket"""

    lottery_win = []
    while len(lottery_win) < 4:
        # Keep from using the same values twice
        pulled_value = choice(lottery_values)
        if pulled_value not in lottery_win:
            lottery_win.append(pulled_value)

    return lottery_win

def ticket_matcher(lottery_win, my_ticket):
    matching_elements = 0
    for my_ticket_value in my_ticket:
        if my_ticket_value is in lottery_win:
            matching_elements += 1

    if matching_elemnts == 4:
        Print(
            f"We finally have a winning ticket "
            " after {attempt_count} attempts!"
            )
    else:
        attempt_count += 1

def my_ticket_attempts(lottery_win):
    """
    Count the amount of attempts until
    my_ticket matches winning_ticket
    """

    my_ticket = []
    while len(my_ticket) < 4:
        pulled_value = choice(lottery_values)
        if pulled_value not in my_ticket:
            my_ticket.append(pulled value)

    return my_ticket



my_ticket_attempts(lottery_win)