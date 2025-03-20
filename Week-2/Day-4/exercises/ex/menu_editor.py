from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("\n--- Program Menu ---")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit the program")
    
    choice = input("Please choose an option: ").upper()
    
    if choice == 'V':
        view_item()
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        remove_item_from_menu()
    elif choice == 'U':
        update_item_from_menu()
    elif choice == 'S':
        show_restaurant_menu()
    elif choice == 'E':
        print("Exiting the program.")
        show_restaurant_menu()
        exit()
    else:
        print("Invalid choice. Please try again.")
        show_user_menu()

def view_item():
    item_name = input("Enter the name of the item you want to view: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        print(f"Item: {item.name}, Price: {item.price}")
    else:
        print(f"Item '{item_name}' not found.")

def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = int(input("Enter the price of the item: "))
    new_item = MenuItem(name, price)
    new_item.save()
    print(f"Item '{name}' was added successfully.")

def remove_item_from_menu():
    name = input("Enter the name of the item you want to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print(f"Item '{name}' was deleted successfully.")
    else:
        print(f"Error: Item '{name}' not found.")

def update_item_from_menu():
    name = input("Enter the name of the item you want to update: ")
    item = MenuManager.get_by_name(name)
    if item:
        new_name = input(f"Enter the new name for '{name}': ")
        new_price = int(input(f"Enter the new price for '{name}': "))
        item.update(new_name, new_price)
        print(f"Item '{name}' was updated successfully.")
    else:
        print(f"Error: Item '{name}' not found.")

def show_restaurant_menu():
    print("\n--- Restaurant Menu ---")
    items = MenuManager.all_items()
    if items:
        for item in items:
            print(f"Item: {item.name}, Price: {item.price}")
    else:
        print("No items available in the menu.")
