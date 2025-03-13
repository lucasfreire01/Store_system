from src import DatabaseInventory
from src import Customer
from src import Employee
def main():
    
    db = DatabaseInventory()
    db.create_base_inventory('inventory')
    db.create_base_inventory('Users')
    db.create_base_inventory('orders')
    #db.add_user('lucas', 'lucas123', 'freirelucas011@gmail.com', False, description_user='Maneger')
    #db.remove_user(user_id='CbMV-')
    #db.update_user(description='supplier', user_id='CbMV-')
    db.add_item(name='Air Max One', category_id='Shoods',description='the first shood', sku=10, price=100.99)
    #db.update_item(name='Shoods', price=90.99, id=5)
    #db.remove_item(id=5)
    #db.add_supplier(name='Freire', email='freirelucas011@gmail.com', phone=38999492824, adress='vasco da gama street')
    #db.update_supplier(name="Lucas Gabriel", id=1)
    #db.remove_supplier(id='3')
    #db.add_order(user_id='E699o', status="Done", total_amount=1, shipping_address='Vasco Da Gama st', billing_address='Vasco Da Gama St')
    #db.update_order(id=3, status='Processing')
    #db.remove_order(id=3)
    #customer = Customer()
    #customer.load(user_id="E699o")
    #customer.verification(name='lucasfreire', password_hash='10.20.30lucas')
    #customer.view_order_history(user_id='E699o')
    #customer.place_orders(user_id='E699o')
    #employee = Employee()
    #employee.get_employee_id(user_id='^.U0Y')
    #employee.load_position(user_id='^.U0Y')


if __name__ == "__main__":
    main()