from db import run_query
from menu_item import MenuItem

class MenuManager:
    
    @classmethod
    def get_by_name(cls, name):
        print(f"Searching for item by name: {name}")
        query = f"SELECT * FROM Menu_Items WHERE item_name = '{name}'"
        result = run_query(query)
        
        if result:
            item = result[0]
            print(f"Item found: {item[1]} with price {item[2]} and id {item[0]}")
            return MenuItem(item[1], item[2], item_id=item[0])
        else:
            print(f"Item with name '{name}' not found")
            return None
        
    @classmethod
    def get_by_id(cls, item_id):
        print(f"Searching for item by name: {item_id}")
        query = f"SELECT * FROM Menu_Items WHERE item_id = '{item_id}'"
        result = run_query(query)
        
        if result:
            item = result[0]
            print(f"Item found: {item[1]} with price {item[2]} and id {item[0]}")
            return MenuItem(item[1], item[2], item_id=item[0])
        else:
            print(f"Item with id '{item_id}' not found")
            return None

    @classmethod
    def all_items(cls):
        print("Retrieving all items from the menu")
        query = "SELECT * FROM Menu_Items"
        results = run_query(query)
        
        items = []
        if results:
            for item in results:
                items.append(MenuItem(item[1], item[2], item_id=item[0]))
            print(f"Total {len(items)} items found")
        else:
            print("No items found in the menu")
        
        return items
