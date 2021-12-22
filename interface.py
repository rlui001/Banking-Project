

def startMenu ():
    """
    Triggers the start menu for a user to use as the interface with the banking system.
    User should enter the corresponding number, otherwise the system repeats the menu.
    """
    print ('-------------------------------------------------------------\n')
    print ('Welcome to the Lui Banking System. Please select an option:  \n')
    print ('1. New customer  \n')
    print ('2. Existing customer  \n')
    print ('3. Employee login  \n')
    print ('4. Exit \n')
    print ('-------------------------------------------------------------\n')

def newCustomer():
    """
    Function to create a new customer and append to database. Returns None.
    """
    pass

def loginCustomer():
    """
    Function to retrieve customer data from database and return as a Customer object.
    """
    pass





if __name__ == "__main__":
    #db connection should be set up here

    startMenu()
