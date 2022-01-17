import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
      return 'It\'s a tie!'

    if win(user, computer):
        return 'You won!'

    return 'You lost'

def win(player, opponent):
    #return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
      return True

print(play())