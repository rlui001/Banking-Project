import helper

class Account:
    
    def __init__ (self, id, balance=0, terminate=False):
        self._id = id
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance
        self._terminate = terminate

    def __str__ (self):
        return f'\nAccount ID: {self._id}\nBalance: {self._balance} \nTermination Status: {self._terminate}\n'

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

    def account_menu(self, conn):
        """Function to call withdraw, deposit, view balance, request termination."""

        menu = """
        Please select an option:  
        1. View balance
        2. Deposit
        3. Withdraw
        4. Request termination
        5. Quit
        """
        print (menu)
        account_updated = False
        while True:
            usr_input = input(f'[Connected - Account ID: {self._id}]: ')
            if usr_input == '1':
                print (f'Your current balance is: {self._balance}')

            elif usr_input == '2':
                deposit_amount = helper.request_input('deposit amount', 'numeric')
                self.deposit(deposit_amount)
                print (f'{deposit_amount} deposited. New balance is {self._balance}')

            elif usr_input == '3':
                withdraw_amount = helper.request_input('withdraw amount', 'numeric')
                self.withdraw(withdraw_amount)
                print (f'{withdraw_amount} withdrawn. New balance is {self._balance}')

            elif usr_input == '4':
                self.terminate()

            elif usr_input == '5':
                print ('Logging off of account.\n')
                return

            print (menu)






class CheckingAccount(Account):

    def __init__ (self, id, balance, rate, terminate):
        """Used when loading result from DB."""
        super(CheckingAccount, self).__init__(id, balance, terminate)
        self._rate = rate
        self._account_type = 'Checking'

    def __str__ (self):
        return f'\nAccount ID: {self._id}\nAccount Type: {self._account_type}\nBalance: {self._balance}\nRate: {self._rate}\nTermination Status: {self._terminate}\n'

    @property
    def rate(self):
        return self._rate
    
    @property
    def account_type(self):
        return self._account_type


class SavingsAccount(Account):

    def __init__ (self, id, balance, rate, terminate):
        """Used when loading result from DB."""
        super(SavingsAccount, self).__init__(id, balance, terminate)
        self._rate = rate
        self._account_type = 'Savings'

    def __str__ (self):
        return f'\nAccount ID: {self._id}\nAccount Type: {self._account_type}\nBalance: {self._balance}\nRate: {self._rate}\nTermination Status: {self._terminate}\n'

    @property
    def rate(self):
        return self._rate
    
    @property
    def account_type(self):
        return self._account_type

