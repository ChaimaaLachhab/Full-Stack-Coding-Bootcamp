#  Exercise 3: Restaurant Menu Manager

class MenuManager:
    def __init__(self):
        """Initialize the menu with predefined dishes."""
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef Bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        """Add a new dish to the menu."""
        new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_dish)
        print(f"{name} has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        """Update an existing dish in the menu."""
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"{name} has been updated.")
                return
        print(f"Error: {name} is not in the menu.")

    def remove_item(self, name):
        """Remove a dish from the menu."""
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"{name} has been removed from the menu.")
                return
        print(f"Error: {name} is not in the menu.")

# Example usage:
menu = MenuManager()
menu.add_item("Pizza", 12, "B", True)
menu.update_item("Salad", 20, "A", False)
menu.remove_item("Soup")
