# Shopping List Manager

shopping_list = []

while True:
    print("\nMenu: add / remove / show / done")
    choice = input("What would you like to do? ").lower()

    if choice == "add":
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print(f"{item} added to your list.")

    elif choice == "remove":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")