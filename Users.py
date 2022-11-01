class Users():

    def __init__(self):
        """Initializes the User class for the microservice.
        It tracks current files in a dictionary for now, but can be
        expanded for larger use cases if needed in the future."""
        self.users = {}  # Init dict for users
        self.current_num = 0  # Count of current users logged in

    def add_user(self, user, data=None):
        """Adds a new user to the list. Can associate
        any data with the user if wanted, but defaults to None.
        Do not include a password as a type of data."""
        
        result = "User is already logged in."

        # Only add user if not already logged in
        if self.verify_unique(user):
            self.users[str(user)] = data
            self.current_num += 1
            result = user + " is now logged in."

        return result



    def verify_unique(self, user):
        """Method that returns False if the given name is already in
        the users dictionary. Otherwise, it will return True."""
        for value in self.users.keys():
            if user == value:
                return False
        
        return True

    def remove_user(self, user, data=None):
        """Removes a new user from the list. Will return any
        data associated with it."""

        result = ""

        # Remove the user if it exists.
        try:
            self.users.pop(user)
            self.current_num -= 1
            result = user + " is now logged out."
        except:
            result = "User not found"


        return result

    def return_current(self):
        return self.current_num

    def update_login_status(self, user):
        """Method that changes the current login status of a user."""
        if self.users[user] is True:
            self.users[user] = False
            self.current_num -= 1
        else:
            self.users[user] = True
            self.current_num += 1


def find_name(json):
    """Function that the value of the name key in the given json.
    If there is no name key, the function will return None."""
    # Find and return the 'name' key in the json
    for key in json:
        if key == "name":
            return json[key]

    # Only returns none if a 'name' key is not found.
    return None