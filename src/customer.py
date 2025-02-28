from .user import User
import sqlite3
from .base import DatabaseInventory
class Customer:

    def __init__(self, address: str, *args):

        super().__init__(*args)

        address = self.address
        order_history = self.load()


    def load(Self):
        connect = sqlite3.connect('database.db')
        user_table = DatabaseInventory.execute("""SELECT * FROM User""")
        orders_table = DatabaseInventory.execute("""SELECT * FROM orders""")

    def verification(self, name=str, password_hash=str):
        query = DatabaseInventory.execute("""SELECT * FROM User(name, password_hash) VALUES(?,?)""", args=(name, password_hash))
        if query is None:
            print('This user not exist')

    def view_order_history(self, user_id:str):
        orders_list = []
        orders_by_user = DatabaseInventory.execute("""SELECT * FROM orders WHERE user_id = ?""", args=(user_id))
        orders_list.append(orders_by_user)
        return orders_list


    def place_orders(self, status=bool, user_id=None):
        status = DatabaseInventory.execute("""SELECT * status WHERE user_id = ?""", args=(user_id))
        if status == 'Done':
            return True
        else:
            return False