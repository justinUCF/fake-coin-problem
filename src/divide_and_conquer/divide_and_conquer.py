# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import math
from tools import scale as scale_module
from tools.scale import scale, scale_phase2

# global variables
genuine_coin = None

# optimized algorithm that preforms the least amount of weighings to find the fake coin. (wrapper)
def divide_and_conquer(prefix, coins):
    global genuine_coin
    genuine_coin = None
    # call phase 1, phase 1 will call phase 2 if neccessary
    start = 0
    end = len(coins)
    fake_coin = divide_and_conquer_phase_1(prefix, start, end)
    # return fake coin
    return fake_coin

# phase one of the optimized algorithm
def divide_and_conquer_phase_1(prefix, start, end):
    global genuine_coin
    # base case, if only one coin left, it is the fake coin
    if((end - start) == 1):
        fake_coin = start
        return fake_coin
    else:
        # identify which indices to split up the coin pile into two equal groups, plus a third group of remaining coins
        size = end - start
        segment_1 = math.ceil(size / 3)
        segment_2 = segment_1 * 2
        # |A| = |B|, |C| is the remaining coins
        offset_1 = start + segment_1
        offset_2 = start + segment_2
        A = (start, offset_1)
        B = (offset_1, offset_2)
        C = (offset_2, end)
        # weigh both A and B, if they are balanced, then the fake coin resides in C, recursively call phase_1
        result = scale(prefix, A, B)
        if result == "balanced":
            if genuine_coin is None:
                genuine_coin = start
            fake_coin = divide_and_conquer_phase_1(prefix, offset_2, end)
        # else if A > B then enter phase 2 with A being the heavy set of coins
        elif result == "left":
            if genuine_coin is None:
                if(end - offset_2 == 0):
                    special_case = (prefix[start + 1]) == (prefix[start + 2] - prefix[start + 1])
                    scale_module.weighings += 1
                    if(special_case):
                        genuine_coin = start
                    else:
                        genuine_coin = offset_1
                else:
                    genuine_coin = offset_2
            fake_coin = divide_and_conquer_phase_2(prefix, B, A)
        # else if A < B then enter phase 2 with B being the heavy set of coins
        elif result == "right":
            if genuine_coin is None:
                if(end - offset_2 == 0):
                    special_case = (prefix[start + 1]) == (prefix[start + 2] - prefix[start + 1])
                    scale_module.weighings += 1
                    if(special_case):
                        genuine_coin = start
                    else:
                        genuine_coin = offset_1
                else:
                    genuine_coin = offset_2
            fake_coin = divide_and_conquer_phase_2(prefix, A, B)
    # found the fake coin in phase 2
    return fake_coin

# phase two of the optimized algorithm
def divide_and_conquer_phase_2(prefix, L, H):
    # base case, if light and heavy groups are only 1 coin each, then fake coin is either in L or H
    if (L[1] - L[0]) == 1 and (H[1] - H[0]) == 1:
        scale_module.weighings += 1
        result = ((prefix[genuine_coin + 1] - prefix[genuine_coin]) == (prefix[L[1]] - prefix[L[0]]))
        if result == True:
            fake_coin = H[0]
        elif result == False:
            fake_coin = L[0]
    else:
        # divide the L group into 2 equal groups and a remainder group
        m = math.ceil((L[1] - L[0])/3)
        L_offset_1 = L[0] + m
        L_offset_2 = L[0] + 2 * m
        L1 = (L[0], L_offset_1)
        L2 = (L_offset_1, L_offset_2)
        L3 = (L_offset_2, L[1])
        # divide the H group into 2 equal groups and a remainder group
        H_offset_1 = H[0] + m
        H_offset_2 = H[0] + 2 * m
        H1 = (H[0], H_offset_1)
        H2 = (H_offset_1, H_offset_2)
        H3 = (H_offset_2, H[1])
        # weigh a combination of both groupings
        result = scale_phase2(prefix, L1, H1, L2, H2)
        if result == "balanced":
            fake_coin = divide_and_conquer_phase_2(prefix, L3, H3)
        elif result == "left":
            fake_coin = divide_and_conquer_phase_2(prefix, L2, H1)
        elif result == "right":
            fake_coin = divide_and_conquer_phase_2(prefix, L1, H2)
    return fake_coin
