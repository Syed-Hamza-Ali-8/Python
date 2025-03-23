def main():
    print("Think of a number between 1 and 100, and I'll try to guess it.\n")
    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("Hmm... something doesn't add up! Did you give the correct hints?")
            break

        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it low(l), high(h), or correct(c) ? ").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        else:
            print("Please enter 'l', 'h', or 'c'.")

    print("Thanks for playing! ")

if __name__ == "__main__":
    main()
