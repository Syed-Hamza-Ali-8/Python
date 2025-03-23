import random

def main():
    print("🏏 Welcome to the Cricket Mad Lib Generator! 🏏\n")
    print("Fill in the blanks to create a funny cricket story!\n")

    batsman = input("Enter your favorite batsman's name: ")
    bowler = input("Enter a famous bowler's name: ")
    team = input("Enter a cricket team name: ")
    
    while True:
        try:
            run = int(input("Enter a number (for runs, between 1 and 500): "))
            if 1 <= run <= 500:
                break
            else:
                print("Please enter a number between 1 and 500.")
        except ValueError:
            print("Please enter a valid number.")
    
    adjective = input("Enter an adjective (e.g., fast, hilarious): ")
    stadium = input("Enter a stadium name: ")

    templates = [
        f"In a thrilling match at {stadium}, {batsman} smashed {run} runs against {team}. The crowd went wild as {bowler} tried to bowl a {adjective} delivery but failed miserably!",
        f"{batsman} walked onto the pitch at {stadium} with confidence. Facing {bowler}'s {adjective} bowling, they hit every ball for a boundary, making {team} fans cheer loudly!",
        f"It was a sunny day at {stadium}. {team} was struggling until {batsman} arrived. Facing {bowler}'s {adjective} bouncers, {batsman} scored {run} runs, leading the team to victory!"
    ]

    story = random.choice(templates)
    
    print("\n🏆 Your Cricket Story:")
    print(story)

if __name__ == "__main__":
    main()
