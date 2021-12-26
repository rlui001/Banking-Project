import helper

class Account:
    
    def __init__ (self, id, balance=0, terminate=False):
        """
        id: customer ssn/account id
        balance: defaults to 0, should be integer
        terminate: defaults to False, can be set to True by customer
        """
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

    @property
    def terminate(self):
        return self._terminate
    
    @terminate.setter
    def terminate(self, val):
        """Updates Account object terminate status."""
        self._terminate = val
    
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
                print (f'\nYour current balance is: {self._balance}')

            elif usr_input == '2':
                deposit_amount = helper.request_input('deposit amount', 'numeric')
                self.deposit(deposit_amount)
                print (f'\n{deposit_amount} deposited. New balance is {self._balance}. Transaction is finalized when logging off.')
                account_updated = True

            elif usr_input == '3':
                withdraw_amount = helper.request_input('withdraw amount', 'numeric')
                self.withdraw(withdraw_amount)
                print (f'\n{withdraw_amount} withdrawn. New balance is {self._balance}. Transaction is finalized when logging off.')
                account_updated = True

            elif usr_input == '4':
                self._terminate = True
                print ('Requested termination. Changes are finalized when logging off.')
                account_updated = True

            elif usr_input == '5':
                if account_updated:
                    print(self)
                    usr_input = input('Account info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    helper.update_db(usr_input, self, conn)
                print ('Logging off of account.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')

            print (menu)






class CheckingAccount(Account):

    def __init__ (self, id, balance=0, rate=0.0, terminate=False):
        """
        id: customer ssn/account id
        balance: defaults to 0, should be integer type
        rate: defaults to 0.0, should be float type
        terminate: defaults to False, can be set to True by customer
        """
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

    def employee_account_menu(self, conn):
        menu = """
        Please select an option:  
        1. Adjust rate
        2. Reset termination status
        3. Quit
        """
        print (menu)
        account_updated = False
        
        while True:
            usr_input = input(f'[Connected - Account ID: {self._id}]: ')

            if usr_input == '1':
                self._rate = helper.request_input('adjusted rate', 'float')
                print (f'\nRate updated: {self._rate}')
                account_updated = True

            elif usr_input == '2':
                self._terminate = False
                print ('\nTermination status reset. Transaction is finalized when logging off.\n')
                account_updated = True

            elif usr_input == '3':
                if account_updated:
                    print(self)
                    usr_input = input('Account info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    helper.update_db(usr_input, self, conn)
                print ('Logging off of account.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')

            print (menu)


class SavingsAccount(Account):

    def __init__ (self, id, balance=0, rate=0.05, terminate=False):
        """
        id: customer ssn/account id
        balance: defaults to 0, should be integer type
        rate: defaults to 0.0, should be float type
        terminate: defaults to False, can be set to True by customer
        """
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

    def employee_account_menu(self, conn):
        pass

