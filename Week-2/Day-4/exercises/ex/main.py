# from db import run_query
# from menu_item import MenuItem
# from menu_manager import MenuManager

# query = '''
# CREATE TABLE IF NOT EXISTS Menu_Items (
#     item_id SERIAL PRIMARY KEY,
#     item_name VARCHAR(30) NOT NULL,
#     item_price SMALLINT DEFAULT 0
# )
# '''
# run_query(query)
# print("Table 'Menu_Items' is ready.")

# item = MenuItem('Burger', 35)
# item.save()

# item.update('Veggie Burger', 37)

# item2 = MenuManager.get_by_name('Beef Stew')
# if item2:
#     print(f"Found item: {item2.name} with price {item2.price}")
# else:
#     print("Item 'Beef Stew' not found")

# items = MenuManager.all_items()
# for i in items:
#     print(f"Item: {i.name} with price {i.price}")

# item.delete()

from menu_editor import show_user_menu

if __name__ == "__main__":
    show_user_menu()
