class BankAccountSimple:
    def __init__(self):
        self.balance = 0

b = BankAccountSimple()
print(b.balance)

# deposit
b.balance += 10
print(b.balance)

# withdraw
b.balance -= 6
print(b.balance)

# withdraw again
b.balance -= 10
print(b.balance)  # what's the problem?

# also: what if we wanted to keep track of a log of transactions?

class BankAccount:
    def __init__(self):
        self._balance = 0
        self._transaction_log = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive! Amount given: {amount}")
        self._balance += amount
        self._log_transaction(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Withdraw amount must be positive! Amount given: {amount}")
        if amount > self._balance:
            raise ValueError(f"Not enough funds to withdraw! Balance: {self._balance}; Amount requested: {amount}")
        self._balance -= amount
        self._log_transaction(-amount)

    def get_balance(self):
        return self._balance

    def _log_transaction(self, amount):
        if amount > 0:
            self._transaction_log.append(f"Deposited {amount}. New balance: {self._balance}")
        else:
            self._transaction_log.append(f"Withdrew {-amount}. New balance: {self._balance}")

    def get_transactions(self):
        return self._transaction_log

# b = BankAccount()
# print(b.get_balance())
#
# # deposit
# b.deposit(10)
# print(b.get_balance())
#
# # withdraw
# b.withdraw(6)
# print(b.get_balance())
#
# # get transaction log
# print(b.get_transactions())

# # withdraw again
# b.withdraw(10)
# print(b.get_balance())

# # deposit invalid amount
# b.deposit(-10)
# print(b.get_balance())

