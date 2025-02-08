#<<<<<<< HEAD
import sqlite3
import random as rd
import string
HARD_CODED_DB = "./database.db"
from datetime import datetime
class Database_inventory:
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
    def execute(self, query, params=True,returnable=False, args=()):

        # open connect
        connect, cursor = self.fetch_database(self.db)

        # execute the query

        if params:
            cursor.execute(query, args)

        else:
            cursor.execute(query)

        # commit
        connect.commit()

        # if have value
      

        if returnable:
            temp = cursor.fetchall()
            print(temp)
            self.close_connection(*(connect, cursor))
            return temp

        self.close_connection(*(connect, cursor))
        # close connection
    
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
            params=False,
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
                params=False,
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
                params=False,
                )
            self.execute(
                """CREATE TABLE IF NOT EXISTS suppliers(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    phone VARCHAR(100) NOT NULL,
                    adress TEXT NOT NULL)
                    """,
                params=False,
                )
        #!!!!!!!!!!!!!Users_tables!!!!!!!!!!!!

        if table == 'Users':
            self.execute(
            """CREATE TABLE IF NOT EXISTS Users(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT NOT NULL,
                       email VARCHAR(255) NOT NULL,
                       has_role INTEGER NOT NULL,
                       password_hash TEXT NOT NULL,
                       role_id TEXT NOT NULL,
                       created_at TIMESTAMP,
                       last_login TIMESTAMP)
                       """,
            params=False,
            )
            self.execute(
                """CREATE TABLE IF NOT EXISTS Roles(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL)""",
            params=False,
            )

        
        #!!!!orders!!!!

        if table == 'orders':
            self.execute(
            """CREATE TABLE IF NOT EXISTS orders(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTERGER,
                       order_date TIMESTAMP,
                       status TEXT NOT NULL,
                       total_amount INTEGER NOT NULL,
                       shipping_address TEXT NOT NULL,
                       billing_address TEXT NOT NULL,
                       create_at TIMESTAMP,
                       update_at TIMESTAMP,
                       FOREIGN KEY (user_id) REFERENCES orders(id))
                       """,
            params=False,
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
            params=False,
        )
            self.execute(
            """CREATE TABLE IF NOT EXISTS orders_status(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       status TEXT NOT NULL)
                       """,
            params=False
            )
        
    def create_view(self, view=None):
        if view == 'inventory_view':
            self.execute(
            """CREATE VIEW IF NOT EXISTS inventory_view AS 
            SELECT
            categories.id AS category_id,
            categories.name AS category_name,
            categories.description AS category_description,
            
            item.id AS item_id,
            item.name AS item_name,
            item.description AS item_description,
            item.category_id AS item_category_id,
            item.sku AS item_sku,
            item.price AS item_price,
            item.supplier_id AS item_supplier_id,
            item.create_at AS item_create_at,
            item.updated_at AS item_updated_at,
            
            inventory.id AS inventory_id,
            inventory.item_id AS inventory_item_id,
            inventory.quantity AS inventory_quantity,
            inventory.location AS inventory_location,
            inventory.reorder_level AS inventory_reorder_level,
            inventory.last_updated AS inventory_last_updated,
            
            suppliers.id AS supplier_id,
            suppliers.name AS supplier_name,
            suppliers.email AS supplier_email,
            suppliers.phone AS supplier_phone,
            suppliers.address AS supplier_address
            
            FROM 
            categories
            LEFT JOIN 
            item ON categories.id = item.category_id
            LEFT JOIN 
            inventory ON item.id = inventory.item_id
            LEFT JOIN 
            suppliers ON item.supplier_id = suppliers.id
            """,
            params=False
            )
        
        if view == 'Users_view':
            self.execute(
                """CREATE VIEW IF NOT EXISTS users_role AS 
                    SELECT
                    Users.id AS user_id,
                    Users.username AS username,
                    Users.email AS email,
                    Users.has_role AS has_role,
                    Users.password_hash AS password_hash,
                    Users.role_id AS role_id,
                    Users.created_at AS created_at,
                    Users.last_login AS last_login,
                    Roles.id AS roles_id,
                    Roles.name AS role_name,
                    Roles.description AS role_description
                    FROM 
                    Users
                    LEFT JOIN 
                    Roles ON Users.has_role = Roles.id
                """,
                params=False
                )
        
        if view == 'orders_view':
            self.execute(
                        """CREATE VIEW IF NOT EXISTS orders_view AS 
                            SELECT
                            orders.id AS orders_id,
                            orders.user_id AS orders_user_id,
                            orders.order_date AS order_date,
                            orders.status AS order_status,
                            orders.total_amount AS order_total_amount,
                            orders.shipping_address AS shipping_address,
                            orders.billing_address AS billing_address,
                            orders.create_at AS order_create_at,
                            orders.update_at AS order_update_at,
                
                            order_items.id AS order_items_id,
                            order_items.order_date AS order_items_date,
                            order_items.item_id AS order_item_id,
                            order_items.quantity AS order_quantity,
                            order_items.price_at_purchase AS order_price,
                
                            order_statuses.id AS statuses_id,
                            order_statuses.status AS statuses_status
                            
                            FROM 
                            orders
                            LEFT JOIN 
                            order_items ON orders.id = order_items.id
                            LEFT JOIN 
                            order_statuses ON orders.status = order_statuses.status
                            """,
                            params=False
                            )
        
    @staticmethod
    def time_for_timestemp():
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    @staticmethod
    def gen_id(n=5):
        printable = string.printable
        return "".join([printable[rd.choice(range(0, len(printable)))] for _ in range(n)])
    def add_user(self, username:str, password_hash:str, email:str, has_role:bool, 
                 id=None, role_id=None, adm_login=bool):
        if adm_login == True:
            def verication():
                password = input('Pleace writing the password: ')
                if password == '12345':
                    return password
                if password != '12345':
                    return print("passord incorrect")
            adm = verication()
            if adm_login is None:
                print('passord is none')
                return
            password_hash = adm
        create_role = role_id if role_id else self.gen_id()
        create_at = self.time_for_timestemp()
        last_login = self.time_for_timestemp()
        has_role_int = 1 if has_role else 0 
        self.execute("""INSERT INTO Users (username, password_hash, email, has_role, role_id,
                     created_at, last_login) VALUES (?,?,?,?,?,?,?)""", args=(username, password_hash, email, has_role_int, create_role,
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

    def add_item(self, id=None, name=str, description=str, category_id=None, sku=int, price=float, supplier_id=None, created_at=None, updated_at=None):
        created_at_item = self.time_for_timestemp()
        updated_at_item = self.time_for_timestemp()
        id_item = id if id else self.gen_id()
        category_id_item = category_id if category_id else self.gen_id()
        supplier_id_item = supplier_id if supplier_id else self.gen_id()
        self.execute("""INSERT INTO item(name, description, sku, price, id, category_id, supplier_id, create_at, updated_at) VALUES(?,?,?,?,?,?,?,?,?)""", args=(name, description, sku,price,
                                                                                                                                      id, category_id_item, supplier_id_item, created_at_item, updated_at_item))
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
        
    def add_supplier(self, id=None, name=str, email=str, phone=int, adress=str):
        id_item = id if id else self.gen_id()
        self.execute("""INSERT INTO suppliers(name, email, phone, adress, id) VALUES(?,?,?,?,?)""", args=(name, email, phone,adress, id))
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
        
