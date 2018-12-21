class Account:
    """ Class representation of a Slushpool Account """

    base_url = "https://slushpool.com/accounts/profile/json/"

    def __init__(self):
        self.username = ""
        self.rating = ""
        self.hashrate = ""
        self.send_threshold = ""
        self.estimated_reward = ""
        self.confirmed_reward = ""
        self.unconfirmed_reward = ""
        self.nmc_send_threshold = ""
        self.unconfirmed_nmc_reward = ""
        self.confirmed_nmc_reward = ""
        self.workers = {}
        self.wallet = ""
