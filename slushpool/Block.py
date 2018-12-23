class Block:
    """ Class Representation of an individual Block """
    def __init__(self, block):
        self.is_mature = block['is_mature']
        self.date_found = block['date_found']
        self.hash = block['hash']
        self.confirmations = block['confirmations']
        self.total_shares = block['total_shares']
        self.total_score = block['total_score']
        self.reward = block['reward']
        self.mining_duration = block['mining_duration']
        self.date_started = block['date_started']
        self.nmc_reward = block['nmc_reward']
