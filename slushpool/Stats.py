class Stats:
    """ Class representation of Slushpool Stats """

    base_url = "https://slushpool.com/stats/json/"

    def __init__(self):
        self.blocks = {}
        self.active_workers = 0
        self.active_stratum = 0
        self.round_started = ""
        self.round_duration = ""
        self.score = ""
        self.shares = 0
        self.shares_cdf = ""
        self.ghashes_ps = ""
        self.luck_30 = ""
        self.luck_b50 = ""
        self.luck_b10 = ""
        self.luck_b250 = ""
        self.luck_7 = ""
        self.luck_1 = ""
