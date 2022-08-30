from sys import float_repr_style
from random import randint

class Budget:

    def __init__(self, category: str, innitial_balance: float):

        self.category = category 
        self.innitial_balance = innitial_balance        
        #private attribute
        self._running_balance = innitial_balance

    def get_running_balance(self): 
        return self._running_balance

    def withdraw(self, amount: float):

        self._running_balance -= amount
        return self._running_balance 

    def deposit(self, amount: float):

        self._running_balance += amount
        return self._running_balance
        
class User:

    def __init__(self, name: str, total_budget: float):

        self.name = name
        self.total_budget = total_budget
        self.id = randint(0, 20)
        self.budgets = {}

    def add_budget(self, category: str, innitial_balance: float):

        budget = Budget(category = category, innitial_balance = innitial_balance)
        self.budgets.update({category: budget})

    def transfer_balance(self, sender: str, receiver: str, amount: float):

        """
        transferenica entre dos categorias
        """

        self.budgets[sender].withdraw(amount = amount)
        self.budgets[receiver].deposit(amount = amount)


