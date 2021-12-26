from sqlalchemy.sql.type_api import UserDefinedType
from helper import *
import logging
import sys


def startMenu():
    """
    Triggers the start menu for a user to use as the interface with the banking system. 
    Returns menu string.
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
    print (customer)
    account = CheckingAccount(ssn)

    stmt_c = "INSERT INTO Customer VALUES (%s, %s, %s, %s)"
    val_c = (customer.ssn, customer.first, customer.last, customer.address)
    stmt_a = "INSERT INTO Account (cid, balance, rate, account_type, terminate) VALUES (%s, %s, %s, %s, %s)"
    val_a = (customer.ssn, account.balance, account.rate, account.account_type, account.terminate)

    #attempt to add record to Customer table
    execute_db(stmt_c, val_c, conn)

    #attempt to add record to Account table
    execute_db(stmt_a, val_a, conn)

    print ('Registered successfully. A checking account has also been created automatically.\n')
    return True

def login(conn, user_type):
    """
    Function to retrieve user data from database and return an Employee object.
    conn: connection to DB
    user_type: String, type of user
    """
    ssn = input('Please enter your SSN to login: ')
    stmt = "SELECT * FROM " + user_type + " WHERE ssn = %s"

    result = execute_db(stmt, ssn, conn, 'first')
    if not result:
        raise ValueError("No user with that SSN found.")

    if user_type == 'Employee':
        return Employee(str(result[0]), result[1], result[2], result[3])

    elif user_type == 'Customer':
        return Customer(str(result[0]), result[1], result[2], result[3])


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, filename='Desktop/Springboard/Banking Project/Logs/messages.log',\
        format='%(asctime)s :: %(levelname)s :: %(message)s')

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
                customer = login(conn, 'Customer')
                print (f'Welcome back to LuiBank, {customer.first}')
                customer.customer_menu(conn)
                break
            elif usr_input == '3':
                employee = login(conn, 'Employee')
                print (f'Welcome back to LuiBank, {employee.first}')
                employee.employee_menu(conn)
                break
            elif usr_input == '4':
                print ('Thank you for using Lui Bank.\n')
                break
            else:
                usr_input = input('Please enter a valid input: ')
        
        print ('System connection terminated...')
