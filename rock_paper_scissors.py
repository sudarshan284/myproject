import random

def play():
    user = input("Welcome to ROck papers and scissors game !! Enter your choice, 'r' for Rock , 'p' for Paper and 's' for Scissors : ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "Its a tie !!!!!"

    if is_win(user,computer):
        return "YOU WON!!!"
    return "You loose"


def is_win(player,opponent):
    if (player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
