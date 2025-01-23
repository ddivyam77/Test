import random

def main():

    wins, losses, ties = 0, 0, 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            wins += 1
            print("You won!")
        elif result == "loss":
            losses += 1
            print("You lost!")
        else:
            ties += 1
            print("It's a tie!")


    print("\nGame over! Here are your stats:")
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

def get_user_choice():

    choices = ["rock", "paper", "scissors", "quit"]
    while True:
        choice = input("Choose rock, paper, scissors, or quit: ").lower()
        if choice in choices:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "loss"

if __name__ == "__main__":
    main()
