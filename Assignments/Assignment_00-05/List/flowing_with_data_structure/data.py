def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    if message:
     print("List before:", my_list)
     add_three_copies(my_list, message)
     print("List after:", my_list)
    else:
     print("I think you are Il-literate")

if __name__ == "__main__":
    main()
