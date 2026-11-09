# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import math
from tools.old.scale import scale

# global variables
genuine_coin = []

# phase two of the optimized algorithm
def divide_and_conquer_phase_2(L, H):
    # base case, if light and heavy groups are only 1 coin each, then fake coin is either in L or H
    if len(L) == 1 and len(H) == 1:
        result = scale(genuine_coin, L)
        if result == "balanced":
            fake_coin = H
        elif result == "left":
            fake_coin = L
    # the fake coin either resides in the L group of coins or the H group of coins
    else:
        # divide the L group into 2 equal groups and a remainder group
        m = math.ceil(len(L)/3)
        L1 = L[:m]
        L2 = L[m:m*2]
        L3 = L[m*2:]
        # divide the H group into 2 equal groups and a remainder group
        H1 = H[:m]
        H2 = H[m:m*2]
        H3 = H[m*2:]
        # weigh a combination of both groupings
        result = scale(L1 + H1, L2 + H2)
        if result == "balanced":
            fake_coin = divide_and_conquer_phase_2(L3, H3)
        elif result == "left":
            fake_coin = divide_and_conquer_phase_2(L2, H1)
        elif result == "right":
            fake_coin = divide_and_conquer_phase_2(L1, H2)
    return fake_coin

# phase one of the optimized algorithm
def divide_and_conquer_phase_1(coin_pile):
    global genuine_coin
    # base case, if only one coin left, it is the fake coin
    if(len(coin_pile) == 1):
        fake_coin = coin_pile
        return fake_coin
    else:
        # identify which indices to split up the coin pile into two equal groups, plus a third group of remaining coins
        segment_1 = math.ceil(len(coin_pile)/3)
        segment_2 = segment_1 * 2    
        # |A| = |B|, |C| is the remaining coins
        A = coin_pile[:segment_1]
        B = coin_pile[segment_1:segment_2]
        C = coin_pile[segment_2:]
        # weigh both A and B, if they are balanced, then the fake coin resides in C, recursively call phase_1
        result = scale(A, B)
        if result == "balanced":
            if not genuine_coin:
                genuine_coin.append(A[0])
            fake_coin = divide_and_conquer_phase_1(C)
        # else if A > B then enter phase 2 with A being the heavy set of coins
        elif result == "left":
            if not genuine_coin:
                genuine_coin.append(C[0])
            fake_coin = divide_and_conquer_phase_2(B, A)
        # else if A < B then enter phase 2 with B being the heavy set of coins
        elif result == "right":
            if not genuine_coin:
                genuine_coin.append(C[0])
            fake_coin = divide_and_conquer_phase_2(A, B)
    # found the fake coin in phase 2
    return fake_coin

# optimized algorithm that preforms the least amount of weighings to find the fake coin.
def divide_and_conquer(coins):
    global genuine_coin
    genuine_coin = []
    # call phase 1, phase 1 will call phase 2 if neccessary
    fake_coin = divide_and_conquer_phase_1(coins)
    # return fake coin    
    return fake_coin
