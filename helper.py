from Account import Account
from Customer import Customer
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
        if isinstance(obj, Account):
            # Build stmt and val for Account record update
            stmt = 'UPDATE Account SET balance = %s, terminate = %s WHERE accountid = %s'
            val = (obj._balance, obj._terminate, obj._id)
            
        elif isinstance(obj, Customer):
            # Build stmt and val for Customer record update
            stmt = 'UPDATE Customer SET first_name = %s, last_name = %s, home_address = %s WHERE ssn = %s'
            val = (obj._first, obj._last, obj._address, obj._ssn)
        else:
            raise TypeError('This class object does not exist.')

        try:
            result = conn.execute(stmt, val)
            if result.rowcount:
                print ('Updated successfully.')
        except:
            print ('Update failed.\n')
    else:
        print ('Changes discarded')

def select_db (stmt, val, conn):
    """
    Function that will return results from DB.
    stmt: String, Raw SQL statement
    val: args being passed
    conn: connection to DB
    """
    pass