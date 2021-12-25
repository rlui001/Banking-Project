from sqlalchemy import create_engine, exc
from helper import *
import sys


def startMenu():
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

    first = request_input('First name', 'alpha')
    last = request_input('Last name', 'alpha')
    address = request_input('Home Address', 'alphanumeric')
    ssn = request_input('Social Security Number', 'numeric')
 
    customer = Customer(ssn, first, last, address)
    print (str(customer))

    stmt_c = "INSERT INTO Customer VALUES (%s, %s, %s, %s)"
    val_c = (customer.ssn, customer.first, customer.last, customer.address)
    stmt_a = "INSERT INTO Account (cid, balance, rate, account_type, terminate) VALUES (%s, %s, %s, %s, %s)"
    val_a = (customer.ssn, 0, 0.0, 'Checking', False)
    try:
        #attempt to add record to Customer table
        conn.execute(stmt_c, val_c)
        try:
            #attempt to add record to Account table
            conn.execute(stmt_a, val_a)
        except exc.SQLAlchemyError as e:
            print (f'failed due to: {e}')
        print ('Registered successfully. A checking account has also been created automatically.\n')
        return True

    except exc.SQLAlchemyError as e:
        print (f"Failed due to: {e}")

def loginCustomer(conn):
    """
    Function to retrieve customer data from database and return a Customer object.
    """

    ssn = input('Please enter your SSN to login: ')
    stmt = "SELECT * FROM Customer WHERE ssn = %s"

    try:
        result = conn.execute(stmt, ssn)
        if not result:
            raise ValueError("No customer with that SSN found.")
        return Customer(str(result[0]), result[1], result[2], result[3])

    except exc.SQLAlchemyError as e:
        print (e)






if __name__ == "__main__":
 
    engine = create_engine('mysql+pymysql://root:password@127.0.0.1/LuiBank')
    with engine.connect() as conn:

        usr_input = input(startMenu())

        while True:

            if usr_input == '1':
                # New customer record created in database
                newCustomer(conn)
                break

            elif usr_input == '2':
                # Customer successfully logins and is able to access customer menu
                customer = loginCustomer(conn)
                print (f'Welcome back to LuiBank, {customer.first}')
                customer.customer_menu(conn)
                break
            elif usr_input == '3':
                print ('Do something with employee')
                break
            elif usr_input == '4':
                print ('Thank you for using Lui Bank.\n')
                break
            else:
                usr_input = input('Please enter a valid input: ')
        
        print ('System connection terminated...')
