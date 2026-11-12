# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
from tools.scale import scale

# global variables
genuine_coin = None

# brute force algorithm used to find a fake coin in at most N/2 weighings
def brute_force(prefix, coins):
    global genuine_coin
    genuine_coin = None
    number_of_coins = len(coins)
    for i in range(0, number_of_coins, 2):
        left_coin = (i, i + 1)
        right_coin = (i + 1, i + 2)
        result = scale(prefix, left_coin, right_coin)
        if(result == "balanced"):
            if(genuine_coin == None):
                genuine_coin = left_coin
            if(i + 2 >= number_of_coins - 1):
                fake_coin = right_coin[1]
                break
        else:
            if(i == 0):
                genuine_coin = (right_coin[0] + 1, right_coin[1] + 1)
            result = scale(prefix, genuine_coin, left_coin)
            if(result == "balanced"):
                fake_coin = right_coin[0]
                break
            else:
                fake_coin = left_coin[0]
                break
    return fake_coin
