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
        self.workers = self.__to_worker_objects(r_json['workers'])
        self.wallet = r_json['wallet']

    def __to_worker_objects(self, workers_json_obj):
        """ Converts the `workers` JSON object values to a dictionary with `Worker` object values.

        This is so worker properties can be accessed like properties instead of dictionary attributes

        `account.workers["name"].alive` instead of `account.workers["name"]["alive"]
        """
        workers = {}

        for worker_name in workers_json_obj:
            workers[worker_name] = Worker(workers_json_obj[worker_name])

        return workers


class Worker:
    """ Class Representation for an individual Worker """
    def __init__(self, worker_json_obj):
        self.last_share = worker_json_obj['last_share']
        self.score = worker_json_obj['score']
        self.alive = worker_json_obj['alive']
        self.shares = worker_json_obj['shares']
        self.hashrate = worker_json_obj['hashrate']
