import random

def main():
    print("===========================================")
    print("Welcome to Rock, Paper, Scissors Game! \n")
    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice not in options:
            print("Invalid choice! Please choose Rock, Paper, or Scissors")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
            break

    print("Thanks for Playing")

if __name__ == "__main__":
    main()
