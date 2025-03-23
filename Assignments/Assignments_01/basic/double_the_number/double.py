def main():
    user_input = int(input("Enter a number: "))

    curr_value = user_input

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == '__main__':
    main()
