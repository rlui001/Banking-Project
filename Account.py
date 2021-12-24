
from typing import Type


class Account:
    
    def __init__ (self, id, balance=0):
        self._id = id
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance
        self._terminate = False

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        try:
            self._balance += int(amount)
        except TypeError:
            raise TypeError('Deposit should be an integer.')

    
    def withdraw(self, amount):
        if not amount.isnumeric():
            raise TypeError('Withdraw should be an integer.')
        elif self._balance - int(amount) < 0:
            raise ValueError('Balance cannot be negative.')
        self._balance -= int(amount)

    def terminate(self):
        # set terminate status to True
        pass
