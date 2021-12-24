from sqlalchemy import create_engine, exc, insert
from Customer import Customer
import sys
import helper


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

def newCustomer(conn):
    """
    Function to create a new customer and append to database. Returns True if successful.
    """

    first = helper.request_input('First name', 'alpha')
    last = helper.request_input('Last name', 'alpha')
    address = helper.request_input('Home Address', 'alphanumeric')
    ssn = helper.request_input('Social Security Number', 'numeric')
 
    customer = Customer(first, last, address, ssn)
    print (str(customer))

    stmt = "INSERT INTO Customer VALUES (%s, %s, %s, %s)"
    val = (customer.ssn, customer.first, customer.last, customer.address)
    try:
        #attempt to add record to Customer table
        conn.execute(stmt, val)
        print ('Registered successfully.\n')
        return True

    except exc.SQLAlchemyError as e:
        print (f"Failed due to: {e}")

def loginCustomer():
    """
    Function to retrieve customer data from database and return as a Customer object.
    """
    pass





if __name__ == "__main__":
 
    engine = create_engine('mysql+pymysql://root:password@127.0.0.1/LuiBank')
    with engine.connect() as conn:

        usr_input = input(startMenu())

        while usr_input != '4':

            if usr_input == '1':
                newCustomer(conn)
                break

            elif usr_input == '2':
                print ('Do something with loginCustomer()')
                break
            elif usr_input == '3':
                print ('Do something with employee')
                break
            else:
                usr_input = input('Please enter a valid input: ')
        
        print ('System connection terminated...')
