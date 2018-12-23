import json
from unittest import TestCase
from unittest.mock import MagicMock

from slushpool import SlushpoolAccount, util
from slushpool.SlushpoolAccount import Worker


class TestSlushpoolAccount(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Mock the fetch_json method to return the sample json instead of making an actual request """
        with open('sample_account.json') as account:
            util.fetch_json = MagicMock(return_value=json.load(account))

    def test_worker_method(self):
        """ Test that SlushpoolAccount.worker("worker") method returns the same as
        SlushpoolAccount.workers["user.worker"]
        """
        account = SlushpoolAccount("token")

        self.assertEqual(account.workers["Username.Worker1"], account.worker("Worker1"))

    def test_workers_are_worker_objects(self):
        """ Test that SlushpoolAccount.workers have been converted to SlushpoolAccount.Worker objects """
        account = SlushpoolAccount("token")
        for worker in account.workers.values():
            self.assertIs(type(worker), Worker)
