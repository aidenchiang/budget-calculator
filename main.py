# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
entertainment = budget.Category("entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
transfer_amount = 20
food_balance_before = food.get_balance()
entertainment_balance_before = entertainment.get_balance()
good_transfer = food.transfer(transfer_amount, entertainment)
food_balance_after = food.get_balance()
entertainment_balance_after = entertainment.get_balance()
print(food.ledger[2])
print({"amount": -transfer_amount, "description": "Transfer to Entertainment"})


#print(create_spend_chart([food, clothing, auto]))
# Run unit tests automatically
main(module='test_module', exit=False)