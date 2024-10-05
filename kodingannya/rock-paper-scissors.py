import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose your option: rock, paper, or scissors.")

    player_choice = input("Enter your choice: ").lower()

    if player_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Start the game
rock_paper_scissors()
