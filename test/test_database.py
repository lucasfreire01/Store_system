import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.base import DatabaseInventory
from src.customer import Customer
if __name__ == "__main__":
    db = DatabaseInventory()
    db.create_base_inventory('inventory')
    db.create_base_inventory('Users')
    db.create_base_inventory('orders')
    db.add_user('lucas', 'lucas123', 'freirelucas011@gmail.com', False)
    #db.remove_user(7)
    db.update_user(password_hash='Lucas102030', id=1)
    db.add_role(name='Produto_1', description='First Product')
    #db.add_item(name='Air Max One', category_id='Shoods',description='the first shood', sku=10, price=100.99)
    #db.update_item(name='Shoods', price=90.99, id=5)
    #db.remove_item(id=5)
    db.add_supplier(name='Freire', email='freirelucas011@gmail.com', phone=38999492824, adress='vasco da gama street')
    #db.update_supplier(name="Lucas Gabriel", id=1)
    #db.remove_supplier(id='3')
    #db.add_order(user_id='jaql5', status="Done", total_amount=1, shipping_address='Vasco Da Gama st', billing_address='Vasco Da Gama St')
    #db.update_order(id=3, status='Processing')
    #db.remove_order(id=3)
    customer = Customer(address='vasco da gama')
    customer.load()