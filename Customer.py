import enum
from typing import Type
import helper
from Account import CheckingAccount, SavingsAccount
from MyService import Services

class Customer:

    def __init__ (self, ssn, first, last, address):
        """
        first: String argument, first name of customer
        last: String argument, last name of customer
        address: String argument, address of customer
        ssn: String argument, converts to int for attribute type
        """
        self._first = first
        self._last = last
        self._address = address
        if len(ssn) == 9:
            try:
                self._ssn = int(ssn)
            except ValueError:
                raise ValueError('Social security number should be digits only.')
        else:
            raise ValueError('Social security number should consist of 9 digits.')

    def __str__ (self):
        return f'Name: {self._first} {self._last} \nAddress: {self._address} \nSSN: {self._ssn}\n'
            
    @property
    def first (self):
        return self._first

    @first.setter
    def first (self, first):
        self._first = first

    @property
    def last (self):
        return self._last

    @last.setter
    def last (self, last):
        self._last = last

    @property
    def address (self):
        return self._address

    @address.setter 
    def address (self, address):
        self._address = address

    @property
    def ssn (self):
        return self._ssn
    
    def customer_menu (self, conn):
        '''Prints the customer menu and loops until exception or user signs out.'''
        menu = """
        Please select an option:  
        1. Update first name
        2. Update last name
        3. Update address
        4. Access accounts
        5. Create a savings account
        6. Services
        7. Quit
        """
        customer_updated = False
        print (menu)
        while True:
            usr_input = input(f'[Connected - {self._first}]: ')

            if usr_input == '1':
                self._first = helper.request_input('First name', 'alpha')
                print ('First name updated.\n')
                customer_updated = True
                
            elif usr_input == '2':
                self._last = helper.request_input('Last name', 'alpha')
                print ('Last name updated.\n')
                customer_updated = True
                
            elif usr_input == '3':
                self._address = helper.request_input('Home Address', 'alphanumeric')
                print ('Address updated.\n')
                customer_updated = True
                
            elif usr_input == '4':
                # sql pull from database to grab existing accounts
                stmt = "SELECT * FROM Account WHERE cid = %s"
                result = helper.execute_db(stmt, self._ssn, conn, 'fetchall')
                print (['Selection: ' + str(i) + ' - ' + row['account_type'] for i, row in enumerate(result)])

                # user selects which account to access 
                usr_input = helper.request_input('Selection #', 'numeric')

                # load into account object
                try:
                    accountid = result[int(usr_input)][0]
                    balance = result[int(usr_input)][2]
                    rate = result[int(usr_input)][3]
                    account_type = result[int(usr_input)][4]
                    terminate = result[int(usr_input)][5]

                    if account_type == 'Checking':
                        account = CheckingAccount(accountid, balance, rate, terminate)
                    elif account_type == 'Savings':
                        account = SavingsAccount(accountid, balance, rate, terminate)
                    print (account)
                    # access account menu
                    account.account_menu(conn)
                except Exception as e:
                    print (e)

            elif usr_input == '5':
                # pull from DB where account_type = 'Savings'
                stmt = "SELECT * FROM Account WHERE cid = %s AND account_type = %s"
                val = (self._ssn, 'Savings')
                result = helper.execute_db(stmt, val, conn, 'first')

                # if result is true then deny request
                if result:
                    print ('Sorry, you already have a Savings account.\n')
                # else create account
                else:
                    account = SavingsAccount(self._ssn)
                    stmt = "INSERT INTO Account (cid, balance, rate, account_type, terminate) VALUES (%s, %s, %s, %s, %s)"
                    val = (account.id, account.balance, account.rate, account.account_type, account.terminate)
                    helper.execute_db(stmt, val, conn)
                    print ('Savings account created successfully.')

            elif usr_input == '6':
                usr_input = helper.request_input('selection (view/request)', 'alpha')
                if usr_input == 'view':
                    # pull from Services table where cid = user ssn and service_status != Rejected
                    stmt = "SELECT * FROM Services WHERE cid = %s AND service_type <> %s"
                    val = (self._ssn, 'Rejected')
                    result = helper.execute_db(stmt, val, conn, 'fetchall')
                    if result:
                        print (['Selection: ' + str(i) + ' - ' + row['service_type'] + ' - ' + row['service_status'] for i, row in enumerate(result)])

                        # user selects which account to access 
                        usr_input = helper.request_input('Selection #', 'numeric')

                        # load into Services object
                        try:
                            serviceid = result[int(usr_input)][0]
                            balance = result[int(usr_input)][2]
                            service_type = result[int(usr_input)][3]
                            service_status = result[int(usr_input)][4]
                            rate = result[int(usr_input)][5]

                            service = Services(serviceid, service_type, balance, service_status, rate)
                            print (service)

                            # access service menu
                            service.customer_services_menu(conn)
                        except Exception as e:
                            print (e)
                    else:
                        print ('You currently have no services.\n')
                elif usr_input == 'request':
                    service_type = helper.request_input('Service type', 'alpha')
                    balance = int(helper.request_input('request amount', 'numeric'))
                    service = Services(self._ssn, service_type, balance)

                    stmt = "INSERT INTO Services (cid, balance, service_type, service_status, rate) VALUES (%s, %s, %s, %s, %s)"
                    val = (service.id, service.balance, service.type, service.status, service.rate)
                    helper.execute_db(stmt, val, conn)

                    print ('Service requested successfully.')
                else:
                    print ('Please enter a valid choice.\n')

            elif usr_input == '7':
                if customer_updated:
                    print(self)
                    usr_input = input('Personal info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    helper.update_db(usr_input, self, conn)
                print ('Thank you for using Lui Bank.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')
            print (menu)
            




    

    
