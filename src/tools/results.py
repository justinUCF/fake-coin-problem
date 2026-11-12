# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
from tools import scale

# print method used in debugging
def print_results(prefix, fake_coin, time, count):
    fake_coin_weight = prefix[fake_coin + 1] - prefix[fake_coin]
    if fake_coin_weight < 2:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin_weight} gram. Took {scale.weighings} weighs with {count} coins.")
    else:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin_weight} grams. Took {scale.weighings} weighs with {count} coins.")
    return
