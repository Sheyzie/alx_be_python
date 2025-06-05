#!/usr/bin/env python

# Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_name = input("Enter item name : ")
            if item_name:
                shopping_list.append(item_name)
                print(f"{item_name} added to shopping list")
            else:
                continue
        elif choice == '2':
            # Prompt for and remove an item
            item_name = input("Enter item name : ")
            for item in shopping_list:
                if item == item_name:
                    shopping_list.remove(item_name)
                    print(f"{item_name} removed from shopping list")
                else:
                    print(f"Item: {item_name} not found")
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) > 0:
                x = 0
                for item in shopping_list:
                    print(f"{x + 1}. {item}")
            else:
                print("Shopping list is empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
