# %%
from budget import Budget, User


# %%
# create user
user1 = User(name = "Mateo", total_budget = 10000)

# %%
user1.add_budget(category = "food", innitial_balance = 2000)

# %%
user1.transfer_balance(sender = "rent", receiver = "food", amount = 1000)

# %%
