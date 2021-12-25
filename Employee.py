import helper

class Employee:
    MIN_SALARY = 60000
    def __init__ (self, ssn, first, last, salary):
        """
        ssn: String/int argument, converts to int for attribute type
        first: String argument, first name of customer
        last: String argument, last name of customer
        address: String argument, address of customer
        salary: String/int argument, will be converted regardless
        """
        if len(ssn) == 9:
            try:
                self._ssn = int(ssn)
            except ValueError:
                raise ValueError('Social security number should be digits only.')
        else:
            raise ValueError('Social security number should consist of 9 digits.')
        self._first = first
        self._last = last
        if int(salary) < Employee.MIN_SALARY:
            self._salary = Employee.MIN_SALARY
        else:
            self._salary = int(salary)

    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, first):
        self._first = first

    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, last):
        self._last = last

    @property
    def salary(self):
        return self._salary

    @property
    def ssn(self):
        return self._ssn

    def employee_menu(self, conn):
        """
        Employee menu.
        conn: connection to DB
        """
        menu = """
        Please select an option:  
        1. Update first name
        2. Update last name
        3. Accounts
        4. Services
        5. Accounts - Terminate all requested
        6. Quit
        """
        employee_updated = False
        print (menu)

        while True:
            usr_input = input(f'[Connected - {self._first}]: ')
            if usr_input == '1':
                self._first = helper.request_input('First name', 'alpha')
                print ('First name updated.\n')
                employee_updated = True
                
            elif usr_input == '2':
                self._last = helper.request_input('Last name', 'alpha')
                print ('Last name updated.\n')
                employee_updated = True

            elif usr_input == '3':
                #show all accounts
                #take user input to select account
                #call account.employee_menu() - build this functioon in Account class
                pass

            elif usr_input == '4':
                #show all services
                #take user input to select service
                #call service.employee_menu() - build this function in Service class
                pass

            elif usr_input == '5':
                #show all accounts marked for termination

                #ask for confirmation

                #delete all records marked for termination from DB
                pass

            elif usr_input == '6':
                if employee_updated:
                    print(self)
                    usr_input = input('Employee info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    helper.update_db(usr_input, self, conn)
                print ('Thank you for being a Lui Bank employee.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')
            
            print (menu)
