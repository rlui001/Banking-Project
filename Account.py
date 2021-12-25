
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
        """Updates Account object terminate status to true."""
        # set terminate status to True
        self._terminate = True


class CheckingAccount(Account):

    def __init__ (self, id):
        super(CheckingAccount, self).__init__(id)
        self._rate = 0
        self._account_type = 'Checking'

    @property
    def rate(self):
        return self._rate
    
    @property
    def account_type(self):
        return self._account_type

