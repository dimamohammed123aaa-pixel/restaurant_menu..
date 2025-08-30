menu = {
    "potato": 40,
    "pasta": 60,
    "pizza": 100,
    "chicken": 120,
    "meat": 200
}

def add_item():
    name = input("Enter item name: ").strip().lower()
    if name in menu:
        print(f"{name} already exists in the menu.")
    else:
        try:
            price = float(input("Enter item price: "))
            if price < 0:
                print("Price must be a positive number.")
            else:
                menu[name] = price
                print(f"{name} added with price {price}.")
        except ValueError:
            print("Invalid price! Please enter a number.")

def remove_item():
    name = input("Enter item name to remove: ").strip().lower()
    if name in menu:
        del menu[name]
        print(f"{name} removed from the menu.")
    else:
        print(f"{name} not found in the menu.")

def clear_menu():
    menu.clear()
    print("Menu cleared successfully!")

def search_item():
    name = input("Enter item name to search: ").strip().lower()
    if name in menu:
        print(f"{name} is in the menu with price: {menu[name]} EGP")
    else:
        print(f"{name} not found in the menu.")

def show_menu():
    if not menu:
        print("Menu is empty.")
    else:
        print("\n--- Current Menu ---")
        choice = input("Do you want to show prices? (p/n): ").strip().lower()
        if choice == "p":
            for name, price in menu.items():
                print(f"{name}: {price} EGP")
        else:
            for name in menu.keys():
                print(name)

def show_summary():
    if not menu:
        print("Menu is empty.")
    else:
        total_items = len(menu)
        total_value = sum(menu.values())
        avg_price = total_value / total_items
        print("\n----- Menu Summary -----")
        print(f"Total items: {total_items}")
        print(f"Total value: {total_value} EGP")
        print(f"Average price: {avg_price:.2f} EGP")

def change_price():
    name = input("Enter item name to change price: ").strip().lower()
    if name in menu:
        try:
            new_price = float(input(f"Enter new price for {name}: "))
            if new_price < 0:
                print("Price must be a positive number.")
            else:
                menu[name] = new_price
                print(f"Price of {name} updated to {new_price}.")
        except ValueError:
            print("Invalid price! Please enter a number.")
    else:
        print(f"{name} not found in the menu.")

def main():
    while True:
        print("\n--- Menu Manager ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. Clear menu")
        print("4. Search for item")
        print("5. Show menu")
        print("6. Show summary")
        print("7. Change price")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            clear_menu()
        elif choice == '4':
            search_item()
        elif choice == '5':
            show_menu()
        elif choice == '6':
            show_summary()
        elif choice == '7':
            change_price()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")






if '__name__' == "_main_":
    main()