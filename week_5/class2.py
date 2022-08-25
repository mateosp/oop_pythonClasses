# %%
from datetime import date
from typing import List


class Orange():
    weight = 10

# %%
naranja = Orange()

# %%
naranja.weight

# %%
def sum(a, b):
    c = a + b
    return c

# %%
sum(3, 4)

# %%
def substraction(a: float, b: float):
    c = b - a
    return c 
    
# %%
substraction(5, 3)
# %%
class Orange():
    def __init__(self):
        self.weight = 10

    def print_weight(self):
        print(self.weight)

# %%
laranja = Orange()

# %%
laranja.weight

# %%
laranja.print_weight()

# %%
from datetime import date
from typing import List

class Customer():
    pass

class Basket():
    def __init__(self, location: str, orange):
        self.location = location
        self.orange = orange

    def sell(self, customer: Customer):
        pass

    def discard(self):
        pass

# %%
class Orange():
    def __init__(self, weight: float, orchard: str, date_picked: date, juice_content: float, basket: Basket = None ):
        self.weight = weight
        self.orchard = orchard
        self.date_picked = date_picked
        self.basket = basket
        self.juice_content = juice_content

    def pick(self, basket: Basket):
        pass

    def squeeze(self):
        return self.juice_content


        
# %%
naranja = Orange(
    weight = 15,
    orchard = "Barranquilla",
    date_picked = date.today()
)