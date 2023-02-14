# Brenden Iannetta
# Mr. Brescacin - ICS4U1
# February 13, 2023
{
    # As a final task for the Python Catch-up, you will create a game of "Rock, Paper, Scissors". Two players will play a best of 5 series with a chance to play again.
    #
    # Keep stats of how many each player has won to be displayed at the end when they decide not to play again.
}

"""
pseudocode = {
    while True:
        menuChoice = Ask the user for their menu choice. (play, rules)
    
        player1Wins = amount of wins for player1 (init 0)
        player2Wins = amount of wins for player2 (init 0)
    
        for game in range(5):
            while game is running:
                player1Choice = ask player for rock paper or scissors
                player2Choice = ask player for rock paper or scissors
        
                if player1Choice is the same as player2Choice:
                    tie game
                    continue at loop beginning
                
                if player1Choice is rock:
                    if player2Choice is scissors:
                        player1 wins
                        player2 loses
                        incriment player1Wins
                    else:
                        player1 loses
                        player2 wins
                        incriment player2Wins
                elif player1Choice is paper:
                    if player2Choice is rock:
                        player1 wins
                        player2 loses
                        incriment player1Wins
                    else:
                        player1 loses
                        player2 wins
                        incriment player2Wins
                elif player1Choice is scissors:
                    if player2Choice is paper:
                        player1 wins
                        player2 loses
                        incriment player1Wins
                    else:
                        player1 loses
                        player2 wins
                        incriment player2Wins
                else:
                    raise ValueError()
    
                break
    
        if player1Wins > player2Wins:
            player 1 wins
        else:
            player 2 wins
        
        ask to play again using menu
                
}
"""

# Import random, math, termcolor, os, and time.
import random
import time
import os
from termcolor import cprint, colored

ROUNDS = 5

RULES = f'''Two players face each other and simultaneously reveal one of three hand gestures: rock (fist), paper (open hand), or scissors (two fingers).

Rock beats scissors, scissors beats paper, and paper beats rock.

The winner of each turn is determined by the gesture they chose: the player with the winning gesture earns one point for that turn.

If both players reveal the same gesture, the turn is a tie and neither player earns a point.

After {ROUNDS} turns, the player with the most points wins the game. In case of a tie, additional rounds can be played until there is a winner.
'''

# Clear screen function.
def cls() -> None:
    os.system("clear")


def playMenu(playAgain = False):
    while True:
        prompt = (
            "Would you like to play again? Choose An Option:"
            if playAgain
            else "Welcome to Rock, Paper, Scissors. Choose An Option:"
        )

        cprint(prompt, "blue", attrs=["bold"])

        againPrompt = "\n1. Play Again" if playAgain else "\n1. Launch Game"

        cprint(againPrompt, attrs=["bold"])
        cprint("2. View Rules", attrs=["bold"])
        cprint("3. Exit", "red", attrs=["bold"])

        choice = input("\n> ")

        if choice != "1" and choice != "2" and choice != "3":
            input(
                colored(
                    "\nThat was not a valid input! Try again.\n\nPress [ENTER] to continue.",
                    "red",
                    attrs=["bold"],
                )
            )
            
            cls()

            continue

        cls()
        
        return choice


def getMove(player) -> str:
    while True:
        cprint(f"Player {player}, choose Rock, Paper, or Scissors.\n", "blue", attrs = ["bold"])
        cprint("1. Rock.", attrs = ["bold"])
        cprint("2. Paper.", attrs = ["bold"])
        cprint("3. Scissors.", attrs = ["bold"])
        
        move = input("\n> ")

        if move != "1" and move != "2" and move != "3":
            input(colored("\nThat was not a valid option! Pick a number.\n\nPress [ENTER] to continue.", "red", attrs = ["bold"]))
            
            cls()

            continue

        cls()

        return move


def game() -> int:
    player1Wins = 0
    player2Wins = 0
    
    for round in range(1, ROUNDS + 1):
        while True:
            player1Move = getMove(1)
            player2Move = getMove(2)
            
            if player1Move == player2Move:
                cprint("Tie game!", "yellow", attrs = ["bold"])
                
                input(colored("\nPress [ENTER] to continue.", "green", attrs = ["bold"]))

                cls()

                continue

            winner = None
            
            if player1Move == "1":
                if player2Move == "3":
                    player1Wins += 1
                    winner = 1
                else:
                    player2Wins += 1
                    winner = 2
            elif player1Move == "2":
                if player2Move == "1":
                    player1Wins += 1
                    winner = 1
                else:
                    player2Wins += 1
                    winner = 2
            else:
                if player2Move == "2":
                    player1Wins += 1
                    winner = 1
                else:
                    player2Wins += 1
                    winner = 2

            break

        if player1Wins == 3 or player2Wins == 3:
            return 1 if player1Wins == 3 else 2

        return 1 if player1Wins > player2Wins else 2


def main() -> None:
    totalGames = 0
    
    while True:
        menuChoice = playMenu(totalGames > 0)

        if menuChoice == "1":
            winner = game()

            totalGames += 1
    
            cprint(f"Game over. The winner is Player {winner}!", "blue", attrs = ["bold"])
        elif menuChoice == "2":
            print(RULES)
        else:
            exit(0)

        input(colored("\nPress [ENTER] to continue.", "green", attrs = ["bold"]))
        
        cls()

        continue


if __name__ == "__main__":
    main()