import json
from unittest import TestCase
from unittest.mock import MagicMock

from slushpool import SlushpoolStats, util
from slushpool.SlushpoolStats import Block


class TestSlushpoolAccount(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Mock the fetch_json method to return the sample json instead of making an actual request """
        # tests should be ran in project root which is why this path includes `tests/`
        with open('tests/sample_stats.json') as account:
            util.fetch_json = MagicMock(return_value=json.load(account))

    def test_latest_block_method(self):
        """ Test that the latest_block() method returns the same as the latest block """
        stats = SlushpoolStats()

        self.assertEqual(stats.blocks["555122"], stats.latest_block)

    def test_blocks_are_block_objects(self):
        """ Test that SlushpoolStats.blocks have been converted to SlushpoolAccount.Block objects """
        stats = SlushpoolStats()

        for block in stats.blocks.values():
            self.assertIs(type(block), Block)
