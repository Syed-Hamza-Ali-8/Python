def main():
    numbers: list[int] = [5, 7, 4, 6] 
    print(numbers)

    for i in range(len(numbers)):
        elem = numbers[i]
        numbers[i] = elem * 2 
    print(numbers)

if __name__ == '__main__':
    main()
