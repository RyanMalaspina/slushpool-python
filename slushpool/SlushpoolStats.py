import requests


class SlushpoolStats:
    """ Class representation of Slushpool Stats """

    base_url = "https://slushpool.com/stats/json/"

    def __init__(self, token=""):
        """ Initialize Slushpool statistics

        A token is not required for this endpoint, if no token is provided the `reward` and `nmc_reward` properties of
        the `blocks` will return `0.00000000` instead of a specific account's reward.
        """
        self.url = SlushpoolStats.base_url + token

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

        self.update()

    def update(self):
        r = requests.get(self.url)

        if r.status_code == 401:
            raise RuntimeError("Invalid Slushpool token!")

        r_json = r.json()

        self.blocks = self.__to_block_objects(r_json['blocks'])
        self.active_workers = r_json['active_workers']
        self.active_stratum = r_json['active_stratum']
        self.round_started = r_json['round_started']
        self.round_duration = r_json['round_duration']
        self.score = r_json['score']
        self.shares = r_json['shares']
        self.shares_cdf = r_json['shares_cdf']
        self.ghashes_ps = r_json['ghashes_ps']
        self.luck_30 = r_json['luck_30']
        self.luck_b50 = r_json['luck_b50']
        self.luck_b10 = r_json['luck_b10']
        self.luck_b250 = r_json['luck_b250']
        self.luck_7 = r_json['luck_7']
        self.luck_1 = r_json['luck_1']

    @property
    def last_block(self):
        """ Return stats on the most recent block found by the pool.

        The block height is inserted into the returned object since the API returns the block height as the key to the
        block's stats.
        """

        block_height_list = sorted(list(self.blocks.keys()))
        last_block_height = block_height_list[-1]

        last_block = self.blocks[last_block_height]
        last_block['height'] = last_block_height

        return last_block

    def __to_block_objects(self, blocks_obj):
        """ Converts the `blocks` JSON object values to a dictionary with `Block` object values.

        This is so block properties can be accessed like properties instead of dictionary attributes

        `stats.blocks["height"].is_mature`  instead of `stats.blocks["height"]["is_mature"]
        """
        blocks = {}

        for block_height in blocks_obj:
            blocks[block_height] = Block(blocks_obj[block_height])

        return blocks


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
