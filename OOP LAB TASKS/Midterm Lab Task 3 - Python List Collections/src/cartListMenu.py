

item = []
choice = None
proceed = None
def menu():
   while True:
    print("\n")
    print("Welcome to 7OOP shopping cart")
    print("---------------------")
    print("1. Add Item: ")
    print("2. Search Item: ")
    print("3. Remove an Item: ")
    print("4. View All Item: ")
    print("5. Exit: ")

    choice = input("Enter choice: ")
    if choice == "1":
        proceed = "1"
        while proceed != "0":
            newItem = input("Enter Item: ").upper()
            item.append(newItem)
            proceed = input("\nEnter 0 to Exit 1 to enter another item: ")
            if proceed == "0":
                choice = None
                proceed = None
                break
            else:
                proceed = None


    elif choice == "2":
        while True:
            counter = 0
            search = input("Enter Item Search: ").upper()
            for i in item:
                if search == i:
                    counter +=1

            if counter == 0:
                print("Item not found")
                break

            else:
                print(f"\nItem found: {search}")
                print(f"number of {search}:", counter)
                print("\n")
                proceed = input("\nEnter 0 to proceed to Menu, 1 to search another item: ")
                if proceed == "1":
                    proceed = None
                    search = None

                if proceed == "0":
                    break

    elif choice == "3":

        while True:
            itemMatch = 0
            remove = input("Enter Item to Remove: ").upper()
            for i in item:
                if remove == i:
                    item.remove(remove)
                    itemMatch += 1

            if itemMatch > 0:
                print(f"Item removed: {remove} \n")
                proceed = input("\nEnter 0 to proceed to Menu, 1 to remove another item: ")

                if proceed == "1":
                    proceed = None

                elif proceed == "0":
                    choice = None
                    proceed = None
                    break

            if itemMatch == 0:
                print("Item not found")
                break

    elif choice == "4":
        if len(item) == 0:
            print("Cart is Empty")
        else:
            for i in item:
                print(f"{i}")
            print("\n")
        choice = None

        input("press any key to continue")

    elif choice == "5":
        exit()

    else:
        print("Invalid choice")


menu()
