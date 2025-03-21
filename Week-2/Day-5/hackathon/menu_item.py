from db import run_query

class MenuItem:
    def __init__(self, name, price, item_id=None):
        self.name = name
        self.price = price
        self.id = item_id
        print(f"MenuItem created: {self.name} with price {self.price} & id {self.id}")

    def save(self):
        query = f"""
        INSERT INTO Menu_Items (item_name, item_price) 
        VALUES ('{self.name}', {self.price}) 
        RETURNING item_id
        """
        result = run_query(query)
        
        if result:
            self.id = result[0][0]
            print(f"Item '{self.name}' saved with price {self.price} and id {self.id}")
        else:
            print(f"Failed to save item '{self.name}'")

    def update(self, new_name, new_price):
        if self.id is None:
            print(f"Cannot update item because id is None")
            return
        
        query = f"""
        UPDATE Menu_Items 
        SET item_name = '{new_name}', item_price = {new_price} 
        WHERE item_id = {self.id}
        """
        run_query(query)
        self.name = new_name
        self.price = new_price
        print(f"Item with id {self.id} updated to name: {self.name} and price: {self.price}")

    def delete(self):
        if self.id is None:
            print(f"Cannot delete item because id is None")
            return
        
        query = f"""
        DELETE FROM Menu_Items 
        WHERE item_id = {self.id}
        """
        run_query(query)
        print(f"Item with id {self.id} and name '{self.name}' deleted")
