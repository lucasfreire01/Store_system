from base_rename import Database_inventory
if __name__ == "__main__":
    db = Database_inventory()
    db.create_base_inventory('inventory')
    db.create_base_inventory('Users')
    db.create_base_inventory('orders')
    #db.add_user('lucas', 'lucas123', 'freirelucas011@gmail.com', False,False)
    #db.remove_user(7)
    #db.update_user(password_hash='Lucas102030', id=1)
    #db.add_role(name='Produto_1', description='First Product')
    #db.add_item(name='Shoods', description='the first shood', sku=10, price=100.99)
    db.update_item(name='Shoods', price=90.99, id=5)
    db.remove_item(id=5)