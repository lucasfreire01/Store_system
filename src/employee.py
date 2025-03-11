from .user import User
from .base import DatabaseInventory

class Employee(User):


    db = DatabaseInventory()
    def __init__(self, position: str ,*args):

        db = DatabaseInventory()
        super().__init__(*args)
        employee_id = self.get_employee_id()
        self.db = DatabaseInventory()
        position = self.position

    def get_employee_id(self,  id: None):
        load_id = self.db.execute("""SELECT * FROM suppliers WHERE id_supplier = ?""", args=(id,))