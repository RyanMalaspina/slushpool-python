class Blocks:
    """ Class representation of recent blocks from Slushpool Stats """
    def __init__(self):
        self.blocks = {}


class Block:
    """ Class Representation of an individual Block """
    def __init__(self):
        self.is_mature = 0
        self.date_found = ""
        self.hash = ""
        self.confirmations = 0
        self.total_shares = 0
        self.total_score = 0
        self.reward = ""
        self.mining_duration = 0
        self.date_started = ""
        self.nmc_reward = ""
