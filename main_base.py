from base import Database_inventory
if __name__ == "__main__":
    db = Database_inventory()
    db.create_base_inventory('inventory')
    db.create_base_inventory('Users')
    db.create_base_inventory('orders')
    db.add_user('lucas', 'lucas123', 'freirelucas011@gmail.com', False,False)
    #db.remove_user(7)
    db.update_user(password='Lucas102030', id=1)
    db.add_role(name='Produto_1', description='First Product')