import random

# Generate computer's choice randomly
"""
    Generates the choice of the computer in the Rock-Paper-Scissors game.

    Parameters:
        none.

    Returns:
        str: The choice of the player. Should be one of 'rock', 'paper', or 'scissors'.

    Example:
        >>> computer_makes_choice()
        'rock'
        >>> computer_makes_choice()
        'scissors'
"""

def computer_makes_choice():
   valid_choices = {'rock', 'paper', 'scissors'}
   result = random.choice(list(valid_choices))
   print(result)
   return result

computer_makes_choice()

"""
    Play a round of the Rock-Paper-Scissors game.

    Parameters:
        player1_choice (str): The choice of Player 1. Should be one of 'rock', 'paper', or 'scissors'.
        comp_choice (str): The choice of Computer. Should be one of 'rock', 'paper', or 'scissors'.

    Returns:
        str: The result of the round. It can be one of the following:
             - "Tie" if both players have the same choice.
             - "Player 1 wins" if Player 1's choice wins the round.
             - "Comp wins" if Computer's choice wins the round.

    Example:
        >>> play_rock_paper_scissors('rock', 'paper')
        'Comp wins'
        >>> play_rock_paper_scissors('scissors', 'scissors')
        'Tie'
    """

def play_rock_paper_scissors(player_choice, comp_choice):
   if player_choice == comp_choice:
       result = "Tie"
   elif (player_choice == 'rock' and comp_choice == 'scissors'
         or player_choice == 'paper' and comp_choice == 'rock'
         or player_choice == 'scissors' and comp_choice == 'paper'):
       result = "Player 1 wins"
   else:
       result = "Comp wins"
   print(result)
   return result

print(play_rock_paper_scissors('rock', 'paper'))


"""
    Play multiple rounds of the Rock-Paper-Scissors game against the computer.

    Parameters:
        num_rounds (int): The number of rounds to play.

    Returns:
        None

    Example:
        >>> play_multiple_rounds(3)
        Enter your choice (rock/paper/scissors): rock
        Round 1: You chose rock. Computer chose paper. Comp wins

        Enter your choice (rock/paper/scissors): paper
        Round 2: You chose paper. Computer chose paper. Tie

        Enter your choice (rock/paper/scissors): scissors
        Round 3: You chose scissors. Computer chose rock. Comp wins
"""

def get_choices ():
    player_choice = input('Enter your choice (rock/paper/scissors): ')
    valid_choices = {'rock', 'paper', 'scissors'}
    comp_choice = random.choice(list(valid_choices))
    return {'player': player_choice, 'computer': comp_choice}


def play_round (r):
    choices = get_choices()
    player = choices['player']
    computer = choices['computer']
    if player == computer:
        result = "Tie!"
    elif (player == 'rock' and computer == 'scissors'
        or player == 'paper' and computer == 'rock'
        or player == 'scissors' and computer == 'paper'):
       result = "Player 1 wins"
    else:
       result = "Comp wins"
    print(f"Round {r+1}: You chose: {player}. Computer chose: {computer}. {result}")

def play_multiple_rounds(rounds):
    r = 0
    while r in range(rounds):
        play_round(r)
        r += 1

num_rounds = int(input("Enter the number of rounds to play: "))
play_multiple_rounds(num_rounds)