import requests


class SlushpoolAccount:
    """ Class representation of a Slushpool Account """

    base_url = "https://slushpool.com/accounts/profile/json/"

    def __init__(self, token):
        self.url = SlushpoolAccount.base_url + token

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

        self.update()

    def update(self):
        """ Update the Account properties from Slushpool """
        r = requests.get(self.url)

        if r.status_code == 401:
            raise RuntimeError("Invalid Slushpool token!")

        r_json = r.json()

        self.username = r_json['username']
        self.rating = r_json['rating']
        self.hashrate = r_json['hashrate']
        self.send_threshold = r_json['send_threshold']
        self.estimated_reward = r_json['estimated_reward']
        self.confirmed_reward = r_json['confirmed_reward']
        self.unconfirmed_reward = r_json['unconfirmed_reward']
        self.nmc_send_threshold = r_json['nmc_send_threshold']
        self.unconfirmed_nmc_reward = r_json['unconfirmed_nmc_reward']
        self.confirmed_nmc_reward = r_json['confirmed_nmc_reward']
        self.workers = r_json['workers']
        self.wallet = r_json['wallet']


class Worker:
    """ Class Representation for an individual Worker """
    def __init__(self):
        self.last_share = 0
        self.score = ""
        self.alive = True
        self.shares = 0
        self.hashrate = 0
