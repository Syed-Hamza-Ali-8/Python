def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Error: Index out of range."


def modify_element(lst, index, new_value):
    try:
        old_value = lst[index]
        lst[index] = new_value
        return f"Element at index {index} changed from '{old_value}' to '{new_value}'."
    except IndexError:
        return "Error: Index out of range."


def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Error: Start or end index out of range."
    return f"Sliced list from index {start} to {end}: {lst[start:end]}"

def main():
    my_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Welcome to the Index Game!")
    print("Your list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
            print("Updated list:", my_list)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Thank you for playing the Index Game! Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4")


if __name__ == "__main__":
    main()
