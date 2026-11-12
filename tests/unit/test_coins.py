import unittest
import random
from src.tools.coins import initialize_coins

class TestCoins(unittest.TestCase):

    lengths = [random.randint(3,10000) for _ in range (100)]

    def test_coins_list_length(self):
        for test_length in self.lengths:
            _, coins = initialize_coins(test_length)
            self.assertEqual(len(coins), test_length, f"Failed for N={test_length}")

    def test_prefix_list_length(self):
        for test_length in self.lengths:
            prefix, _ = initialize_coins(test_length)
            self.assertEqual(len(prefix), test_length+1, f"Failed for N={test_length}")

    def test_fake_coin_exists(self):
        for test_length in self.lengths:
            _, coins = initialize_coins(test_length)
            self.assertEqual(len([c for c in coins if c != 2]), 1, f"Failed to generate False coin for N={test_length}")

    def test_fake_coin_weight(self):
        for test_length in self.lengths:
            _, coins = initialize_coins(test_length)
            fake = [c for c in coins if c != 2][0]
            self.assertIn(fake, [1,3], f"Rouge fake coin weight")
            