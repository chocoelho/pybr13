class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def get_account(self, name):
        return self.accounts[name]

    def open_account(self, name, initial_balance):
        signup_bonus = "20.0"
        if name in self.accounts:
            raise RuntimeError(
                "Bank {} already had an account for {}".format(self.name, name)
            )
        self.accounts[name] = Account(name, initial_balance + signup_bonus)

    def deposit(self, name, amount):
        if name in self.accounts:
            account = self.accounts[name]
            return account.deposit(amount)
        else:
            return None

def donate(bank, names, amount_each):
    amount_total = 0.0
    for name in names:
        amount_deposited = bank.deposit(name, amount_each)
        if amount_deposited:
            amount_total += amount_deposited
    return amount_total
