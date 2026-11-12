# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import random

# this function intializes a pile of N coins with one fake coin (either light or heavy). It also precomputes an array of summed weights of contiguous coins named prefix (used throughout the program)
def initialize_coins(N):
    # fill an integer array that represents coins, 2 is the default weight of a genuine coin
    coins = [2] * N
    # randomly select an index within the array to place a fake coin with a weight of either 1 (light) or 3 (heavy)
    fake_coin_index = random.randint(0, N - 1)
    coins[fake_coin_index] = random.choice((1,3))
    # compute a prefix array where each index of the prefix array represents the weights of contiguous coins (this will allow weighing to be an O(1) operation)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + coins[i]
    return prefix, coins
