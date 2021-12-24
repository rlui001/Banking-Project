from sqlalchemy import create_engine
import sys

def startMenu ():
    """
    Triggers the start menu for a user to use as the interface with the banking system. Returns menu string.
    """
    menu = """
    Welcome to the Lui Banking System. Please select an option:  
        1. New customer
        2. Existing customer
        3. Employee login
        4. Exit
    """
    return menu

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
    engine = create_engine('mysql+pymysql://root:password@127.0.0.1/LuiBank')
    print(engine.table_names())


    usr_input = input(startMenu())

    while True:
        if usr_input == '1':
            print ('Do something with newCustomer()')
            break
        elif usr_input == '2':
            print ('Do something with loginCustomer()')
            break
        elif usr_input == '3':
            print ('Do something with employee')
            break
        elif usr_input == '4':
            break
        else:
            usr_input = input('Please enter a valid input: ')
    
    print ('System log off.')
