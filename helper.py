def request_input(req, type):
    """
    Helper function to request input from user and return valid input.
    req: string, input being requested
    type: string, input type expected
    """
    user_input = input(f'Please enter your {req}: ')
    types = {'alpha': user_input.isalpha(), 'numeric': user_input.isnumeric, 'alphanumeric': True}

    #based on the type, will call function from dictionary to determine if criteria is met
    while not types[type]:
        user_input = input(f'Please enter a valid {req}: ')
        # not sure if there is a better way to update the conditionals, this method will use up memory
        types = {'alpha': user_input.isalpha(), 'numeric': user_input.isnumeric}

    return user_input
