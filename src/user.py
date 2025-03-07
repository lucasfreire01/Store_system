from .base import DatabaseInventory
 

class User:

    def __init__(self, name: str, email: str, phone: str):

        assert isinstance(name, str), ""
        assert isinstance(email, str), ""
        assert isinstance(phone, str), ""

        self.name = name
        self.email = email
        self.phone = phone

    def get_name():
        pass

    def login():
        pass

    def logout():
        pass

    def updateProfile():
        pass

    # ETC

    



  