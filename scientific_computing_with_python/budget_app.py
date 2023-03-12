class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        output = ""
        output += self.name.center(30, "*") + "\n"

        total = 0
        for item in self.ledger:
            total += item["amount"]

            output += item["description"].ljust(23, " ")[:23]
            output += "{0:>7.2f}".format(item["amount"])
            output += "\n"
        output += "Total: " + "{0:.2f}".format(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        current_balance = 0
        for item in self.ledger:
            current_balance += item["amount"]
        return current_balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.ledger.append({
                "amount":
                    -amount,
                "description":
                    "Transfer to " + budget_category.name
            })
            budget_category.ledger.append({
                "amount":
                    amount,
                "description":
                    "Transfer from " + self.name
            })
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_money_out(self):
        current_balance = 0
        for item in self.ledger:
            if (item["amount"] < 0) and ("transfer" not in item["description"].lower()):
                current_balance += abs(item["amount"])

        return current_balance


def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    category_names = []
    len_category_names = 0
    category_expenses = []
    category_percentage = []
    category_percentage_rounded = []

    for category in categories:
        category_expenses.append(category.get_money_out())
        category_names.append(category.name)
        if len(category.name) > len_category_names:
            len_category_names = len(category.name)

    category_expenses_total = sum(category_expenses)

    for expense in category_expenses:
        p = ((((expense / category_expenses_total) * 10) // 1) * 10)
        category_percentage.append(p)

    for p in category_percentage:
        category_percentage_rounded.append(int(round(p, 2)))

    category_names_justified = []
    for name in category_names:
        category_names_justified.append(name.ljust(len_category_names, " "))

    for i in range(100, -1, -10):
        output += str(i).rjust(3, " ") + '|'
        for p in category_percentage_rounded:
            if p >= i:
                output += " o "
            else:
                output += "   "
        output += " \n"

    output += "    " + "-" * (3 * len(category_names_justified)) + "-\n"

    for i in range(len_category_names):
        output += "    "
        for name in category_names_justified:
            output += " " + name[i] + " "
        else:
            output += " \n"

    return output.strip("\n")
  
