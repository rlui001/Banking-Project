import helper

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
        7. Request account termination
        8. Quit
        """
        customer_updated = False

        while True:
            usr_input = input(f'[Connected - {self._first}]: ')

            if usr_input == '1':
                self._first = helper.request_input('First name', 'alpha')
                print ('First name updated.\n')
                customer_updated = True
                pass
            elif usr_input == '2':
                self._last = helper.request_input('Last name', 'alpha')
                print ('Last name updated.\n')
                customer_updated = True
                pass
            elif usr_input == '3':
                self._address = helper.request_input('Home Address', 'alphanumeric')
                print ('Address updated.\n')
                customer_updated = True
                pass
            elif usr_input == '4':
                # sql pull from database to grab existing accounts
                # user selects which account to access 
                # load into account object
                # allow modification of account object
                # push changes to db
                pass
            elif usr_input == '5':
                # request input for savings account object
                # create account object
                # push insert to db
                pass
            elif usr_input == '6':
                # request/view services
                # pick service type
                # pick amount request
                # submit to db which needs to be approved
                pass
            elif usr_input == '7':
                # sql pull from database to grab existing accounts
                # user selects which account to terminate
                # request is sent in to DB to update status
                pass
            elif usr_input == '8':
                if customer_updated:
                    print(str(self))
                    usr_input = input('Personal info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    if usr_input.lower() != 'n':
                        stmt = 'UPDATE Customer SET first_name = %s, last_name = %s, home_address = %s WHERE ssn = %s'
                        val = (self._first, self._last, self._address, self._ssn)
                        try:
                            result = conn.execute(stmt, val)
                            if result.rowcount:
                                print ('Updated successfully.')
                        except:
                            print ('Update failed.\n')
                    else:
                        print ('Changes discarded.')
                print ('Thank you for using Lui Bank.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')
            




    

    
