class Workers:
    """ Class Representation of Workers object for a Slushpool Account """

    def __init__(self):
        self.workers = {}


class Worker:
    """ Class Representation for an individual Worker """
    def __init__(self):
        self.last_share = 0
        self.score = ""
        self.alive = True
        self.shares = 0
        self.hashrate = 0
