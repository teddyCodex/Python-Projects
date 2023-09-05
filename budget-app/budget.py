class Category:
    def __init__(self, name) -> None:
        self.category_name = name.title()
        self.ledger = list()

    def deposit(self, amount, desc=str()):
        payload = {"amount": amount, "description": desc}
        self.ledger.append(payload)

    def withdraw(self, amount, desc=str()):
        if self.check_funds(amount=amount):
            payload = {"amount": -amount, "description": desc}
            self.ledger.append(payload)
            return True
        else:
            return False

    def get_balance(self):
        amounts = [item.get("amount") for item in self.ledger]
        balance = sum(amounts)
        return round(balance, 2)

    def transfer(self, amount, category_name):
        if self.check_funds(amount=amount):
            self.withdraw(float(amount), f"Transfer to {category_name.category_name}")
            category_name.deposit(float(amount), f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        current_balance = self.get_balance()
        return amount <= current_balance

    def __repr__(self) -> str:
        ledger = self.ledger
        output = str()
        for item in ledger:
            description = item.get("description")
            amount = item.get("amount")
            amount = str("%0.2f" % amount)
            if len(description) < 23:
                space = " "
                output += f"{description}{space * (23 - len(description))}{space * (7 - len(amount))}{amount}\n"
            else:
                output += f"{description[:23]} {amount}\n"

        balance = self.get_balance()

        return f"""*************{self.category_name}*************\n{output}Total: {balance}"""


def create_spend_chart(categories):
    # Helper function to calculate percentage spent
    def get_withdrawals(category):
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return -total

    # Calculate total spent and individual spent percentages
    total_spent = sum([get_withdrawals(cat) for cat in categories])
    spent_percentages = [
        (cat, int(get_withdrawals(cat) / total_spent * 100)) for cat in categories
    ]

    # Build the bar chart
    chart = "Percentage spent by category\n"

    # Building the vertical bars
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for _, percent in spent_percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Horizontal line below bars
    chart += "    -" + "---" * len(categories) + "\n"

    # Category names written vertically below bars
    max_name_length = max([len(cat.category_name) for cat in categories])
    for i in range(max_name_length):
        chart += "     "
        for cat, _ in spent_percentages:
            if i < len(cat.category_name):
                chart += cat.category_name[i] + "  "
            else:
                chart += "   "
        chart = f"{chart}\n"

    return chart.rstrip() + "  "
