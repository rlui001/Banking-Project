class Services:
    def __init__(self, id, type, status='Initiated', rate=0):
        """
        id: customer ssn
        type: service type being requested
        status: defaults to Initiated. Employee sets to Pending once rate is given, or Rejected if declined.
        rate: defaults to 0, to be updated by employee
        """
        self._id = id
        self._type = type
        self._status = status
        self._rate = rate

    def __str__ (self):
        return f'\Service ID: {self._id}\nService Type: {self._type} \nService Status: {self._status} \nService Rate: {self._rate}\n'

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

    @property
    def type(self):
        return self._type

    def customer_services_menu(self, conn):
        """
        Customer services menu to request/view/update a service.
        conn: connection to DB
        """
        pass

    def employee_services_menu(self, conn):
        """
        Employee services menu to view/update a service.
        conn: connection to DB
        """
        pass

    
