#<<<<<<< HEAD
import sqlite3
import random as rd
import string
HARD_CODED_DB = "./database.db"
from datetime import datetime


class DatabaseInventory:
    def __init__(self, DB=None):
        self.db = HARD_CODED_DB if DB is None else DB

    
    @staticmethod
    def fetch_database(dir):
        connect = sqlite3.connect(dir)
        cursor = connect.cursor()
        return connect, cursor
    
    @staticmethod
    def close_connection(connect, cursor):
        cursor.close()
        connect.close()
    #create a execute to open make the method and close to imporve the memory use 

    @staticmethod
    def time_for_timestemp():
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    @staticmethod
    def gen_id(n=5):
        printable = string.printable
        return "".join([printable[rd.choice(range(0, len(printable)))] for _ in range(n)])

    def execute(self, query, args=(), returnable=False):
        if not isinstance(args, tuple):
            args = (args,) 

        connect, cursor = self.fetch_database(self.db)


        cursor.execute(query, args)


        connect.commit()


        if returnable:
            temp = cursor.fetchall()
            print(temp) 
            self.close_connection(*(connect, cursor))
            return temp


        self.close_connection(*(connect, cursor))

    
    def create_base_inventory(self, table:str = None):
        if table is None:
            print('Dataset if not name')
        
        if table == 'inventory':
            self.execute(
            """CREATE TABLE IF NOT EXISTS category(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(100) NOT NULL,
                       description VARCHAR(255))
                       """,
            )
            self.execute(
            """CREATE TABLE IF NOT EXISTS item(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL,
                description VARCHAR(255),
                category_id INTEGER,
                sku VARCHAR(36) NOT NULL,
                price INTEGER NOT NULL,
                supplier_id INTEGER,
                create_at TIMESTAMP,
                updated_at TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES category(id),
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
                )""",
            )
            self.execute(
                """CREATE TABLE IF NOT EXISTS inventory(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_id INTEGER,
                    quantity INTEGER NOT NULL,
                    location TEXT NOT NULL,
                    reorder_level INTEGER NOT NULL,
                    last_updated TIMESTAMP,
                    FOREIGN KEY (item_id) REFERENCES item(id))
                    """,
                )
            self.execute(
                """CREATE TABLE IF NOT EXISTS suppliers(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_supplier TEXT NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    phone VARCHAR(100) NOT NULL,
                    adress TEXT NOT NULL)
                    """,
                )
        #!!!!!!!!!!!!!Users_tables!!!!!!!!!!!!

        if table == 'Users':
            self.execute(
            """CREATE TABLE IF NOT EXISTS Users(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id TEXT NOT NULL,
                       username TEXT NOT NULL,
                       email VARCHAR(255) NOT NULL,
                       has_role INTEGER NOT NULL,
                       password_hash TEXT NOT NULL,
                       role_id TEXT NOT NULL,
                       created_at TIMESTAMP,
                       last_login TIMESTAMP)
                       """,
            )
            self.execute(
                """CREATE TABLE IF NOT EXISTS Roles(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL)""",
            )

        
        #!!!!orders!!!!

        if table == 'orders':
            self.execute(
            """CREATE TABLE IF NOT EXISTS orders(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id TEXT NOT NULL,
                       order_date TIMESTAMP,
                       status TEXT NOT NULL,
                       total_amount INTEGER NOT NULL,
                       shipping_address TEXT NOT NULL,
                       billing_address TEXT NOT NULL,
                       create_at TIMESTAMP,
                       update_at TIMESTAMP,
                       FOREIGN KEY (user_id) REFERENCES orders(id))
                       """,
        )          
            self.execute(
            """CREATE TABLE IF NOT EXISTS orders_items(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       order_date TIMESTAMP,
                       item_id INTERGER,
                       quantity INTEGER NOT NULL,
                       price_at_purchase INTERGER NOT NULL,
                       FOREIGN KEY (item_id) REFERENCES order_items(id))
                       """,
        )
            self.execute(
            """CREATE TABLE IF NOT EXISTS orders_status(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       status TEXT NOT NULL)
                       """,
            )
        
    def add_user(self, username:str, password_hash:str, email:str, has_role:bool, role_id=2, user_id=None):

        assert role_id is not None and isinstance(role_id, int) and role_id in range(1, 3), "please provide an integer"

        # colocar as outras asserções
       
        create_user = self.gen_id()
        create_at = self.time_for_timestemp()
        last_login = self.time_for_timestemp()
        self.execute("""INSERT INTO Users (username, password_hash, email, has_role, role_id, user_id,
                     created_at, last_login) VALUES (?,?,?,?,?,?,?,?)""", args=
                     (username, password_hash, email,has_role, role_id,create_user,
                                                      create_at, last_login))

    def update_user(self, id:str, username = None, password_hash = None, email = None, has_role = None):
        if username is not None:
            self.execute("""UPDATE Users SET username = ? WHERE  id = ?""", args=(username, id))
        
        if password_hash is not None:
            self.execute("""UPDATE Users SET password_hash = ? WHERE  id = ?""", args=(password_hash, id))
        
        if email is not None:
            self.execute("""UPDATE Users SET email = ? WHERE  id = ?""", args=(email, id))
        
        if has_role is not None:
            self.execute("""UPDATE Users SET has_role = ? WHERE  id = ?""", args=(has_role, id))
    
    def remove_user(self, id:str):
        self.execute("""DELETE FROM Users WHERE id = ?""", args=(id,))
    
    def add_role(self,id:str=None,name=None, description=None):
        self.execute("""INSERT INTO Roles (name, description) VALUES(?,?)""", args=(name, description))

    def add_item(self, id=None, name=str, description=str, category_id=str, sku=int, price=float, supplier_id=None, created_at=None, updated_at=None, supplier_keep=False, supplier_share=None):
        if supplier_keep == True:
            supplier = self.execute("""SELECT id FROM suppliers WHERE id = ?""", args=(supplier_share,))
            supplier_id = supplier
        created_at_item = self.time_for_timestemp()
        updated_at_item = self.time_for_timestemp()
        id_item = id if id else self.gen_id()
        supplier_id_item = supplier_id if supplier_id else self.gen_id()
        self.execute("""INSERT INTO item(name, description, sku, price, id, category_id, supplier_id, create_at, updated_at) VALUES(?,?,?,?,?,?,?,?,?)""", args=(name, description, sku,price,
                                                                                                                                      id, category_id, supplier_id_item, created_at_item, updated_at_item))
    def update_item(self, name=str, description=None, sku=None, price=None, id=None):
        if name is not None:
            self.execute("""UPDATE item SET name = ? WHERE id= ?""", args=(name, id))
        if description is not None:
            self.execute("""UPDATE item SET description = ? WHERE id= ?""", args=(description, id))
        if sku is not None:
            self.execute("""UPDATE item SET sku = ? WHERE id= ?""", args=(sku, id))
        if price is not None:
            self.execute("""UPDATE item SET price = ? WHERE id= ?""", args=(price, id))

    def remove_item(self, id=str):
        self.execute("""DELETE FROM item WHERE id = ?""", args=(id,))
        
    def add_supplier(self, id=None, name=str, email=str, phone=int, adress=str, id_supplier=None):
        id_supplier = id if id else self.gen_id()
        self.execute("""INSERT INTO suppliers(name, email, phone, adress, id, id_supplier) VALUES(?,?,?,?,?,?)""", args=(name, email, phone,adress, id, id_supplier))
    def update_supplier(self, id=int, name=None, email=None, phone=None, adress=None):
        if name is not None:
            self.execute("""UPDATE suppliers SET name = ? WHERE id= ?""", args=(name, id))
        if email is not None:
            self.execute("""UPDATE suppliers SET email = ? WHERE id= ?""", args=(email, id))
        if phone is not None:
            self.execute("""UPDATE suppliers SET phone = ? WHERE id= ?""", args=(phone, id))
        if adress is not None:
            self.execute("""UPDATE suppliers SET adress = ? WHERE id= ?""", args=(adress, id))

    def remove_supplier(self, id=str):
        self.execute("""DELETE FROM suppliers WHERE id = ?""", args=(id,))
    
    def add_order(self, id=None, user_id = None, order_date=None, status=str, total_amount=int, shipping_address=str, billing_address=str, create_at=None, update_at=None):
        user_id = user_id if user_id else self.gen_id()
        order_date = self.time_for_timestemp()
        create_at = self.time_for_timestemp()
        update_at = self.time_for_timestemp()
        self.execute("""INSERT INTO orders (user_id, order_date, status, total_amount, shipping_address, billing_address,
                     create_at, update_at) VALUES (?,?,?,?,?,?,?,?)""", args=(user_id, order_date, status, total_amount, shipping_address, billing_address,
                                                      create_at, update_at))

    def update_order(self, id:str, user_id = None, status = None, total_amount = None, shipping_address = None, billing_address=None):
        if user_id is not None:
            self.execute("""UPDATE orders SET user_id = ? WHERE  id = ?""", args=(user_id, id))
        
        if status is not None:
            self.execute("""UPDATE orders SET status = ? WHERE  id = ?""", args=(status, id))
        
        if total_amount is not None:
            self.execute("""UPDATE orders SET total_amount = ? WHERE  id = ?""", args=(total_amount, id))
        
        if shipping_address is not None:
            self.execute("""UPDATE orders SET shipping_address = ? WHERE  id = ?""", args=(shipping_address, id))
        
        if billing_address is not None:
            self.execute("""UPDATE orders SET billing_address = ? WHERE id = ?""", args=(billing_address, id))
    
    def remove_order(self, id:str):
        self.execute("""DELETE FROM orders WHERE id = ?""", args=(id,))