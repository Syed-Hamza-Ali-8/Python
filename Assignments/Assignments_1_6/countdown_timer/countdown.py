import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Countdown Timer: {timer}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

def main():
    print("===================================")
    print("       Countdown Timer App         ")
    print("===================================\n")
    
    try:
        total_seconds = int(input("Enter time in seconds: "))
        clear_screen()
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid input! Please enter an integer")

if __name__ == "__main__":
    main()
