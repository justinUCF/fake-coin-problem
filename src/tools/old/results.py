# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
from tools.old import scale

# print result function
def print_results(fake_coin, time):
    if fake_coin[0] < 2:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin[0]} gram. Took {scale.weighings} weighs.")
    else:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin[0]} grams. Took {scale.weighings} weighs.")
