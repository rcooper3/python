import random

def main():
    show_header()

    player = "You"
    ai = "Computer"

    play_game(player, ai)

def show_header():
    print("--------------------------")
    print("ROCK, PAPER, SCISSORS v1")
    print("--------------------------")

def play_game(player_1, player_2):

    # player_1 = input("Enter Player 1 Name: ")
    # player_2 = input("Enter Player 2 Name: ")
    # player_1 = "You"
    # player_2 = "Computer"

    rolls = ["ROCK", "PAPER", "SCISSORS"]

    roll1 = get_roll(player_1, rolls)
    roll2 = random.choice(rolls)

    if not roll1:
        print("Can't play that, exiting")
        return

    print(f"{player_1} Player 1 rolls {roll1}")
    print(f"{player_2} Player 2 rolls {roll2}")

    # Test for a winner
    winner = None

    if roll1 == roll2:
        print(f"The play was tied!")
    elif roll1 == "ROCK" and roll2 == "PAPER":
        winner = player_2
    elif roll1 == "ROCK" and roll2 == "SCISSORS":
        winner = player_1
    elif roll1 == "PAPER" and roll2 == "SCISSORS":
        winner = player_2
    elif roll1 == "PAPER" and roll2 == "ROCK":
        winner = player_1
    elif roll1 == "SCISSORS" and roll2 == "PAPER":
        winner = player_1
    elif roll1 == "SCISSORS" and roll2 == "ROCK":
        winner = player_2

    print("The game is over!")
    if winner is None:
        print("It was a tie!")
    else:
        print(f"The winner is {winner}")

def get_roll(player_name, rolls):
    roll = input(f"{player_name}, What is your Roll ? [ROCK, PAPER, SCISSORS]: ")
    roll = roll.upper().strip()
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid roll")
        return None
    return roll

if __name__ == '__main__':
    main()