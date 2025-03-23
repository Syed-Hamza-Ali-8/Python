def main():
    number = int(input("Enter any number: "))

    if number != 0:
        for i in range(number, 0, -1):
            print(i, end=" ")
        print("\nLiftoff!")
    else:
        print("Zero is not allowed!")

if __name__ == '__main__':
    main()
