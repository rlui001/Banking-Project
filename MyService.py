import helper

class Services:
    def __init__(self, id, type, balance, status='Initiated', rate=0.0):
        """
        id: customer ssn/account id
        type: service type being requested
        status: defaults to Initiated. Employee sets to Pending once rate is given, or Rejected if declined.
        rate: defaults to 0.0, to be updated by employee
        """
        self._id = id
        self._type = type
        if balance < 0:
            raise ValueError('Balance cannot be 0.\n')
        self._balance = balance
        self._status = status
        self._rate = rate

    def __str__ (self):
        return f'\nService ID: {self._id}\nService Type: {self._type}\nBalance: {self._balance}\nService Status: {self._status} \nService Rate: {self._rate}\n'

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        return self._balance

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status
        
    @status.setter
    def status(self, input):
        """
        input: initiated, rejected, pending, accepted are the only acceptable statuses
        """
        if input.lower() == 'rejected':
            self._status = 'Rejected'
        elif input.lower() == 'pending':
            self._status = 'Pending'
        elif input.lower() == 'accepted':
            self._status = 'Accepted'
        elif input.lower() == 'initiated':
            self._status = 'Initiated'
        else:
            raise ValueError('Invalid status type for this service.\n')

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        try:
            self.rate = float(rate)
        except TypeError:
            raise TypeError('Invalid type for rate.\n')

    def customer_services_menu(self, conn):
        """
        Customer services menu to request/view/update a service.
        conn: connection to DB
        """
        menu = """
        Please select an option:  
        1. Accept service terms
        2. Reject service terms
        3. Update request amount
        4. Quit
        """
        if self._status == 'Accepted':
            print ('This service has already been accepted. You can only view the terms:\n')
            print (self)
            input('Enter any key to return back to customer menu...\n')
            return

        service_updated = False
        print (menu)
        while True:
            usr_input = input(f'[Connected - Service ID {self._id}]: ')

            if usr_input == '1':
                if self._status == 'Initiated':
                    print ('You cannot accept this until it has been reviewed by an employee.\n')
                else:
                    self._status = 'Accepted'
                    print (f'Status set to {self._status}. Status will be updated during log off.')
                    service_updated = True

            elif usr_input == '2':
                self._status = 'Rejected'
                print (f'Status set to {self._status}. Status will be updated during log off.')
                service_updated = True

            elif usr_input == '3':
                balance = helper.request_input('new request amount', 'numeric')
                self._balance = int(balance)
                self._status = 'Initiated'
                print (f'Request amount set to {self._balance}. Balance will be updated during log off.')
                service_updated = True

            elif usr_input == '4':
                if service_updated:
                    print(self)
                    usr_input = input('Service info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    helper.update_db(usr_input, self, conn)
                print ('Logging off of service.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')

            print (menu)



    def employee_services_menu(self, conn):
        """
        Employee services menu to view/update a service.
        conn: connection to DB
        """
        menu = """
        Please select an option:  
        1. Adjust rate (automatically sets to Pending)
        2. Adjust balance (automatically sets to Pending)
        3. Mark Pending
        4. Reject
        5. Quit
        """
        if self._status == 'Accepted':
            print ('This service has already been accepted. You can only view the terms:\n')
            print (self)
            input('Enter any key to return back to customer menu...\n')
            return

        if self._status == 'Rejectede':
            print ('This service has already been rejected. You can only view the terms:\n')
            print (self)
            input('Enter any key to return back to customer menu...\n')
            return

        service_updated = False
        print (menu)
        while True:
            usr_input = input(f'[Connected - Service ID {self._id}]: ')

            if usr_input == '1':
                self._rate = helper.request_input('adjusted rate', 'alphanumeric')
                self._status = 'Pending'
                print (f'\nRate updated: {self._rate}')
                service_updated = True

            elif usr_input == '2':
                self._balance = helper.request_input('adjusted balance', 'numeric')
                self._status = 'Pending'
                print (f'Balance set to {self._balance}. Balance will be updated during log off.')
                service_updated = True

            elif usr_input == '3':
                self._status = 'Pending'
                print (f'Status set to {self._status}. Status will be updated during log off.')
                service_updated = True

            elif usr_input == '4':
                self._status = 'Rejected'
                print (f'Status set to {self._status}. Status will be updated during log off.')
                service_updated = True

            elif usr_input == '5':
                if service_updated:
                    print(self)
                    usr_input = input('Service info was updated. If the changes above are incorrect, type N to discard changes. Otherwise, enter anything to proceed: \n')
                    helper.update_db(usr_input, self, conn)
                print ('Logging off of service.\n')
                return
            else:
                print ('Invalid input. Please try again.\n')

            print (menu)

    
