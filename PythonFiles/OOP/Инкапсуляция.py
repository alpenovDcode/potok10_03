class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

my_account = BankAccount()
my_account.deposit(50)
print(my_account.get_balance())


# Java
# public, static, private, protected

# m1 __a, def __say_hello()
# m2 import m1