from .user import User
from .base import DatabaseInventory

class Employee:


    db = DatabaseInventory()
    def __init__(self,*args):

        db = DatabaseInventory()
        super().__init__(*args)
        self.db = DatabaseInventory()
    def get_employee_id(self,  user_id: None):
        load_id = self.db.execute("""SELECT * FROM Users WHERE user_id = ?""", args=(user_id,))
    
    def load_position(self,  user_id: None):
        load_id = self.db.execute("""SELECT description FROM Roles WHERE user_id = ?""", args=(user_id,))

    #def managerInventory(self, )