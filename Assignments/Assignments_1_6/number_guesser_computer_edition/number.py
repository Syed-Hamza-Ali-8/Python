import random

def main():
    print("========================================================")
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a valid number.")


    print("Thank you for playing! ")

if __name__ == "__main__":
    main()
