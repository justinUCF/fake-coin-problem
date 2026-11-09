# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
from tools.old.scale import scale

# brute force algorithm to find the fake coin within a pile of coins
def brute_force(coins):
    # count the number of coins
    coin_pile = len(coins)
    # place holder for weighing each coin individually, two at a time
    left_coin = [0]
    right_coin  = [0]
    # weigh two coins against each other, if they balance move on to the next two coins to weigh
    for i in range(coin_pile):
        j = i + 1
        left_coin = [coins[i]]
        right_coin = [coins[j]]
        result = scale(left_coin, right_coin)
        # if result is balanced than we have not found the position of the fake coin
        if result == "balanced":
            continue
        # fake coin is either in position i or j
        elif result == "left" and i == 0:
            genuine_coin = [coins[j + 1]]
            result = scale(left_coin, genuine_coin)
            if result != "balanced":
                return left_coin
            else:
                return right_coin
        # fake coin is in position j    
        elif result == "left" and i > 0:
            return right_coin
        # fake coin is either in position i or j
        elif result == "right" and i == 0:
            genuine_coin = [coins[j + 1]]
            result = scale(left_coin, genuine_coin)
            if result != "balanced":
                return left_coin
            else:
                return right_coin
        # fake coin is in position j
        elif result == "right" and i > 0:
            return right_coin
