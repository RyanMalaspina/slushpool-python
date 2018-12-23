from slushpool.SlushpoolStats import SlushpoolStats
from slushpool.SlushpoolAccount import SlushpoolAccount


class Slushpool:
    """ Class Representation of Slushpool API Endpoints

    The Account endpoint requires a token to generate a response, so if no token is provided `account` is set to `None`.
    """
    def __init__(self, token=""):
        self.stats = SlushpoolStats(token)

        if token != "":
            self.account = SlushpoolAccount(token)
        else:
            self.account = None

    def update(self):
        """ Update stats and account information from Slushpool. """
        self.stats.update()

        if self.account is not None:
            self.account.update()
