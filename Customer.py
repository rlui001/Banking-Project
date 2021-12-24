class Customer:

    def __init__ (self, first, last, address, ssn):
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
    

    

    
