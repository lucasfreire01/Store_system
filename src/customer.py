import sqlite3
from .base import DatabaseInventory
class Customer:

    db = DatabaseInventory()
    def __init__(self, *args):

        super().__init__(*args)
        db = DatabaseInventory()
        self.db = DatabaseInventory()


    def load(self,user_id: str):
        print(user_id)
        user_table = self.db.execute("""SELECT * FROM Users WHERE user_id = ?""", (user_id,))
        orders_table = self.db.execute("""SELECT * FROM orders WHERE user_id = ?""", (user_id,))
        address_table = self.db.execute("""SELECT shipping_address FROM orders WHERE user_id = ?""", (user_id,))

    def verification(self, name: str, password_hash: str):
        query = self.db.execute("""SELECT * FROM Users WHERE username = ? AND password_hash = ? """, args=(name, password_hash))
        if query is None:
            print('These information not match')

    def view_order_history(self, user_id:str):
        orders_list = []
        orders_by_user = self.db.execute("""SELECT * FROM orders WHERE user_id = ?""", args=(user_id,))
        orders_list.append(orders_by_user)
        return orders_list

    def place_orders(self, status=bool, user_id=None):
        status = self.db.execute("""SELECT status FROM orders WHERE user_id = ?""", args=(user_id))
        print(status)
        if status == 'Done':
            return True
        else:
            return False