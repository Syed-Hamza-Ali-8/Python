import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hangman():
    word_list = ["python", "developer", "programming", "javascript", "streamlit", "hackathon", "laptop"]
    word = random.choice(word_list)
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    while len(word_letters) > 0 and tries > 0:
        clear_screen()
        print("=====================================")
        print("       Welcome to Hangman Game!       ")
        print("=====================================")
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Tries Left: {tries}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed! Press Enter to continue...")
            input()
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            guessed_letters.add(guess)
            tries -= 1

    clear_screen()
    if tries == 0:
        print(f"Game Over! The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}' correctly!")

if __name__ == "__main__":
    hangman()
