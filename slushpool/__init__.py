from slushpool.Stats import Stats
from slushpool.Account import Account


class Slushpool:
    """ Class Representation of Slushpool API Endpoints

    The Account endpoint requires a token to generate a response, so if no token is provided `account` is set to `None`.
    """
    def __init__(self, token=""):
        self.stats = Stats(token)

        if token != "":
            self.account = Account(token)
        else:
            self.account = None
