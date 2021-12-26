import re
import helper
from MyService import Services
from Account import CheckingAccount, SavingsAccount
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
                self.access_accounts(conn)

            elif usr_input == '4':
                self.access_services(conn)
                pass

            elif usr_input == '5':
                self.terminate_accounts(conn)

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

    def terminate_accounts(self, conn):
        """
        Function to delete all accounts marked for termination.
        conn: connection to DB
        """
        # show all accounts marked for termination
        stmt = "SELECT * FROM Account WHERE terminate = %s"
        val = 1
        result = helper.execute_db(stmt, val, conn, 'fetchall')
        # if there are results
        if result:
            print ('\n'.join(['Selection: ' + str(i) + ' - ' + row['account_type'] + ' - ' + str(row['terminate']) for i, row in enumerate(result)]))
        # ask for confirmation
            if input('Please enter "confirm" to delete all accounts marked for termination: ') == 'confirm':
                stmt_del = "DELETE FROM Account WHERE terminate = %s"
                helper.execute_db(stmt_del, val, conn)
                print ('Accounts deleted.\n')
            else:
                print ('Accounts were not deleted.\n')
        else:
            print ('There are currently no accounts marked for termination.\n')

    def access_accounts(self, conn):
        #show all accounts
        stmt = "SELECT * FROM Account"
        try:
            result = conn.execute(stmt).fetchall()
        except:
            raise Exception('Unable to select records from Account table.\n')
        if result:
            print ('\n'.join(['Selection: ' + str(i) + ' - Customer SSN: ' + str(row['cid']) + ' - Type: ' + row['account_type'] for i, row in enumerate(result)]))
        
            # user selects which account to access 
            usr_input = helper.request_input('Selection #', 'numeric')
            # load into account object
            account = helper.load_account_object(usr_input, result)
                
            account.employee_account_menu(conn)

        else:
            print ('There are no accounts.\n')

    def access_services(self, conn):
        #show all accounts
        stmt = "SELECT * FROM Services"
        try:
            result = conn.execute(stmt).fetchall()
        except:
            raise Exception('Unable to select records from Services table.\n')
        if result:
            print ('\n'.join(['Selection: ' + str(i) + ' - Customer SSN: ' + str(row['cid']) + ' - Type: ' + row['service_type'] + ' - Status: ' + row['service_status'] for i, row in enumerate(result)]))
        
            # user selects which account to access 
            usr_input = helper.request_input('Selection #', 'numeric')
            # load into Services object
            service = helper.load_services_object(usr_input, result)
            
            service.employee_services_menu(conn)

        else:
            print ('There are no services.\n')