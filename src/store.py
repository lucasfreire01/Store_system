from .base import DatabaseInventory
class Order:
    def __init__(self, *args):
        db = DatabaseInventory()

        db = DatabaseInventory()
        super().__init__(*args)
        self.db = DatabaseInventory()

    def load_order(self, order_date=None, status=None, custumer=None, order_list = None, 
                   total_amount=None):
        load_orders = self.db.execute("""SELECT order_id AND order_date FROM orders WHERE user_id = ?""", args=())