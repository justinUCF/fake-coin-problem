# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregros and Justin Gamboa

# imports
import random
import math

weighings = 0

# this function intializes a pile of N coins based on user input (N), then randomly selects an index to place either a light or heavy fake coin randomly.
def initialize_coins():
    while True:
        number_of_coins = int(input("Enter the amount of coins: "))
        if number_of_coins >= 3:
            break
        print("Number of coins must be greater than 3.")
    coins = [2] * number_of_coins
    fake_coin_index = random.randint(0, number_of_coins - 1)
    coins[fake_coin_index] = random.choice((1,3))
    
    # hard coded test case
    # coins = [2,1,2,2,2,2] 
    
    return coins

# function that weighs two piles of coins. Returns "left" to indicate left is heavier, "right" to indicate right is heavier, or "balanced" to indicate both sides weigh the same.
def scale(left, right):
    global weighings
    weighings += 1
    left_side = sum(left)
    right_side = sum(right)
    if left_side > right_side:
        return "left"
    elif right_side > left_side:
        return "right"
    elif left_side == right_side:
        return "balanced"    

# phase two of the optimized algorithm
def divide_and_conquer_phase_2(L, H):
    # base case, if light and heavy groups are only 1 coin each, then fake coin is either in L or H
    if len(L) == 1 and len(H) == 1:
        result = scale([2], L)
        if result == "balanced":
            fake_coin = H
        elif result == "left":
            fake_coin = L
    else:
        m = math.ceil(len(L)/3)
        L1 = L[:m]
        L2 = L[m:m*2]
        L3 = L[m*2:]
        H1 = H[:m]
        H2 = H[m:m*2]
        H3 = H[m*2:]
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

        # weigh both A and B, if they are balanced, then the fake coin resides in C, recursively call phase_1 until 
        result = scale(A, B)

        if result == "balanced":
            fake_coin = divide_and_conquer_phase_1(C)
        # else if A > B then enter phase 2 with A being the heavy set of coins
        elif result == "left":
            fake_coin = divide_and_conquer_phase_2(B, A)
        # else if A < B then enter phase 2 with B being the heavy set of coins
        elif result == "right":
            fake_coin = divide_and_conquer_phase_2(A, B)
    # found the fake coin in phase 2
    return fake_coin

# optimized algorithm that preforms the least amount of weighings to find the fake coin.
def divide_and_conquer_wrapper(coins):
    # call phase 1
    fake_coin = divide_and_conquer_phase_1(coins)
    # return fake coin    
    return fake_coin

# print result function
def print_results(pile, fake):
    if fake[0] < 2:
        print(f"Fake coin identified to be lighter with a weight of: {fake[0]} in {weighings} weighs")
    else:
        print(f"Fake coin identified to be heavier with a weight of: {fake[0]} in {weighings} weighs")

# main executable function
def main():
    coins = initialize_coins()
    result = divide_and_conquer_wrapper(coins)
    print_results(coins, result)

# control mechanism to execute main
if __name__ == "__main__":
    main()