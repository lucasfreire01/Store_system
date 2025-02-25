from .user import User

class Employee(User):


    def __init__(self, position: str ,args*):

        super().__init__(args*)
        employee_id = self.get_employee_id()
        position = self.position

    def get_employee_id(self):
        pass