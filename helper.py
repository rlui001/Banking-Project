from typing import Type
from sqlalchemy import create_engine, exc
from sqlalchemy.sql.functions import user
from Account import *
from Customer import Customer
from MyService import Services
from Employee import Employee

def request_input(req, type):
    """
    Helper function to request input from user and return valid input.
    req: string, input being requested
    type: string, input type expected
    """
    user_input = input(f'Please enter your {req}: ')
    types = {'alpha': user_input.isalpha(), 'numeric': user_input.isnumeric(), 'alphanumeric': True}

    #based on the type, will call function from dictionary to determine if criteria is met
    while not types[type]:
        if type == 'float':
            try:
                return float(user_input)
            except TypeError:
                raise TypeError('Input type is incorrect.\n')

        user_input = input(f'Please enter a valid {req}: ')
        # not sure if there is a better way to update the conditionals, this method will use up memory
        types = {'alpha': user_input.isalpha(), 'numeric': user_input.isnumeric()}

    return user_input

def update_db (usr_input, obj, conn):
    """
    Handles database record update.
    usr_input: user input determines whether update occurs
    obj: Class object passed in
    conn: connection to DB
    """
    if usr_input.lower() != 'n':
        if isinstance(obj, (CheckingAccount, SavingsAccount)):
            # Build stmt and val for Account record update
            stmt = 'UPDATE Account SET balance = %s, terminate = %s , rate = %s WHERE accountid = %s'
            val = (obj._balance, obj._terminate, obj._rate, obj._id)
            
        elif isinstance(obj, Customer):
            # Build stmt and val for Customer record update
            stmt = 'UPDATE Customer SET first_name = %s, last_name = %s, home_address = %s WHERE ssn = %s'
            val = (obj._first, obj._last, obj._address, obj._ssn)

        elif isinstance(obj, Services):
            # Build stmt and val for Services record update
            stmt = 'UPDATE Services SET balance = %s, service_status = %s, rate = %s WHERE serviceid = %s'
            val = (obj._balance, obj._status, obj._rate, obj._id)

        elif isinstance(obj, Employee):
            # Build stmt and val for Employeee record update
            stmt = 'UPDATE Employee SET first_name = %s, last_name = %s WHERE ssn = %s'
            val = (obj._first, obj._last, obj._ssn)
        else:
            raise TypeError('This class object does not exist.')

        execute_db(stmt, val, conn)
    else:
        print ('Changes discarded')

def execute_db (stmt, val, conn, op=''):
    """
    Function that will return results from DB.
    stmt: String, Raw SQL statement
    val: args being passed
    conn: connection to DB
    op: first, fetchall, update
    """
    if op == 'first':
        try:
            result = conn.execute(stmt, val).first()
        except exc.SQLAlchemyError as e:
            raise Exception(f'Failed due to: {e}')
    elif op == 'fetchall':
        try:
            result = conn.execute(stmt, val).fetchall()
        except exc.SQLAlchemyError as e:
            raise Exception(f'Failed due to: {e}')
    else:
        try:
            result = conn.execute(stmt, val)
        except exc.SQLAlchemyError as e:
            raise Exception(f'Failed due to: {e}')

    return result

def load_services_object(usr_input, result):
    """
    Load and return a Services object
    usr_input: String, user selection
    result: list of results from query
    """
    # load into Services object
    try:
        serviceid = result[int(usr_input)][0]
        balance = result[int(usr_input)][2]
        service_type = result[int(usr_input)][3]
        service_status = result[int(usr_input)][4]
        rate = result[int(usr_input)][5]

        service = Services(serviceid, service_type, balance, service_status, rate)
        print (service)
        return service
    except Exception as e:
        print (e)