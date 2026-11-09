# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import random

# this function intializes a pile of N coins based on user input (N), then randomly selects an index to place either a light or heavy fake coin randomly.
def initialize_coins(N):
    # fill an integer array that represents coins, 2 is the default weight of a genuine coin
    coins = [2] * N
    # randomly select an index within the array to place a fake coin with a weight of either 1 (light) or 3 (heavy)
    fake_coin_index = random.randint(0, N - 1)
    coins[fake_coin_index] = random.choice((1,3))
    return coins
