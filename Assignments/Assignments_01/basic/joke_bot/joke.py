PROMPT: str = "What do you want? "
JOKE: str = "Why did the Python programmer go broke? Because he used up all his cache!"
SORRY: str = "Sorry I only tell jokes."

def main():
    print("Simply write joke in the field")
    print("=========================================")
    user_input = input(PROMPT)
    user_input = user_input.strip().lower()
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
