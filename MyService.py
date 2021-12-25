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
        return f'\Service ID: {self._id}\nService Type: {self._type}\nBalance: {self._balance}\nService Status: {self._status} \nService Rate: {self._rate}\n'

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
        if input.lower() == 'rejected':
            self._status = 'Rejected'
        elif input.lower() == 'pending':
            self._status = 'Pending'
        elif input.lower() == 'accepted':
            self._status = 'Accepted'
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
        4. Access accounts
        5. Create a savings account
        6. Services
        7. Quit
        """

        pass

    def employee_services_menu(self, conn):
        """
        Employee services menu to view/update a service.
        conn: connection to DB
        """
        pass

    
