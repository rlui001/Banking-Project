
class Account:
    
    def __init__ (self, id, balance=0):
        self._id = id
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance
        self._terminate = False

    def __str__ (self):
        return f'\nBalance: {self._balance} \nTermination Status: {self._terminate}\n'

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
        """Updates Account object terminate status to true."""
        # set terminate status to True
        self._terminate = True


class CheckingAccount(Account):

    def __init__ (self, id):
        super(CheckingAccount, self).__init__(id)
        self._rate = 0
        self._account_type = 'Checking'

    def __str__ (self):
        return f'\nAccount Type: {self._account_type}\nBalance: {self._balance}\nRate: {self._rate}\nTermination Status: {self._terminate}\n'

    @property
    def rate(self):
        return self._rate
    
    @property
    def account_type(self):
        return self._account_type


class SavingsAccount(Account):

    def __init__ (self, id):
        super(SavingsAccount, self).__init__(id)
        self._rate = 0.05
        self._account_type = 'Savings'

    def __str__ (self):
        return f'\nAccount Type: {self._account_type}\nBalance: {self._balance}\nRate: {self._rate}\nTermination Status: {self._terminate}\n'

    @property
    def rate(self):
        return self._rate
    
    @property
    def account_type(self):
        return self._account_type

