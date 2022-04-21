class Category:
    name = ""
    totalSpent = 0

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        finalOutput = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            row = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            finalOutput += f'{row}\n'

        finalOutput += "Total: " + str(self.get_balance())
        return finalOutput

    def deposit(self, amount, description=""):
        d = {"amount": float(amount), "description": description}
        self.ledger.append(d)

    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total += item['amount']
        if float(amount) <= total:
            return True
        else:
            return False

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            d = {"amount": float(-amount), "description": description}
            self.ledger.append(d)
            self.totalSpent += amount
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category2):
        if self.check_funds(amount) is True:
            description1 = f'Transfer from {self.name}'
            description2 = f'Transfer to {category2.name}'
            d1 = {"amount": float(-amount), "description": description2}
            self.totalSpent += amount
            self.ledger.append(d1)
            d2 = {"amount": float(amount), "description": description1}
            category2.ledger.append(d2)
            return True
        else:
            return False


def create_spend_chart(categories):
    category = Category
    spent = dict()
    pct_exp = dict()
    total_exp = 0
    for category in categories:
        spent[category.name] = category.totalSpent
        total_exp += category.totalSpent
    for key, value in spent.items():
        pct_exp[key] = value/total_exp*100

    row = "Percentage spent by category"
    for i in range(100, -1, -10):
        row += f'\n{str(i).rjust(3)}|'
        for j in pct_exp.values():
            if j > i:
                row += " o "
            else:
                row += "   "
        row += " "
    row += '\n    ----------'

    length = []
    for category in categories:
        length.append(len(category.name))
    max_length = max(length)

    for i in range(max_length):
        row += "\n    "
        for j in range(len(categories)):
            if i < length[j]:
                row += " " + categories[j].name[i] + " "
            else:
                row += " " * 3
        row += " "

    return row