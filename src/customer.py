from .user import User

class Customer(User):

    def __init__(self, address: str, args*):

        super().__init__(args*)

        address = self.address
        order_history = self.load_orders()


    def load_orders(Self):
        pass
