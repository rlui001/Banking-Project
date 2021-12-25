class Services:
    def __init__(self, id, type, status='Initiated', rate=0):
        """
        id: customer ssn
        type: service type being requested
        status: defaults to Initiated
        rate: defaults to 0, to be updated by employee
        """
        self._id = id
        self._type = type
        self._status = status
        self._rate = rate