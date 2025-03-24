from .base import DatabaseInventory

class item:
    db = DatabaseInventory()
    def __init__(self, *args):

        db = DatabaseInventory()
        super().__init__(*args)
        self.db = DatabaseInventory()

    def load_item(self, item_id:str, name:str, description:str, sku:str, price:float, quantaty_stock:int, 
                  category:str, supplier:str):
        load_dict = dict()
        load_db = self.db.execute("""SELECT """)