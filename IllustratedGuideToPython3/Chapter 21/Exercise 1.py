# Exercise: Imagine you are designing a banking application. What would a customer look like?
# What attributes would she have? What methods would she have?

class BankCustomer:
    '''A Customer in a bank'''

    def __init__(self, balance):
        self._money = balance

    def deposit(self, bank):
        # put money in bank

    def withdraw(self, bank):
        # get money out of bank

    def balance(self):
        # returns current balance
        return self._money
