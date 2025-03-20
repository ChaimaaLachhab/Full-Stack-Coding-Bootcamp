from db import run_query

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"MenuItem created: {self.name} with price {self.price}")
    
    def save(self):
        query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES ('{self.name}', {self.price})"
        run_query(query)
        print(f"Item '{self.name}' saved with price {self.price}")
    
    def update(self, new_name, new_price):
        query = f"UPDATE Menu_Items SET item_name = '{new_name}', item_price = {new_price} WHERE item_name = '{self.name}'"
        run_query(query)
        self.name = new_name
        self.price = new_price
        print(f"Item updated: {self.name} with new price {self.price}")
    
    def delete(self):
        query = f"DELETE FROM Menu_Items WHERE item_name = '{self.name}'"
        run_query(query)
        print(f"Item '{self.name}' deleted")
