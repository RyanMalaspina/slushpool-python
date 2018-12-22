from slushpool.Stats import Stats
from slushpool.Account import Account


class Slushpool:
    """ Class Representation of Slushpool API Endpoints """
    def __init__(self, token):
        self.account = Account(token)
        self.stats = Stats(token)
