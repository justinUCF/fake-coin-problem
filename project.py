# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import random
import math
import time

# global variables
weighings = 0
genuine_coin = []
genuine_coin_new = None

# function in charge of getting user input
def get_user_input():
    print("___________________________________________________________________________________________________________________\n                                    T H E   F A K E   C O I N   P R O B L E M                        \n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n Welcome to the Fake Coin Problem!\n This simulation identifies a single fake coin among N identical weighted coins using two algorithms:\n Brute Force and Divide & Conquer. Genuine coins weigh 2 grams, while a fake coin weighs either 1 gram (light)\n or 3 grams (heavy).\n \n Enter a starting coin count (minimum 3). Both algorithms will run at that count, and each subsequent\n run increases the count by 2,048 coins. Graphs of the results are displayed when the simulation ends.\n___________________________________________________________________________________________________________________\n                                       GIORGIO TORREGROSA & JUSTIN GAMBOA\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
               
    # ensure the user can only create a pile of 3 or more coins
    while True:
        number_of_coins = int(input("Enter the amount of coins: "))
        if number_of_coins >= 3:
            break
        print("Number of coins must be greater than 3.")
    return number_of_coins

# this function intializes a pile of N coins based on user input (N), then randomly selects an index to place either a light or heavy fake coin randomly.
def initialize_coins(N):
    # fill an integer array that represents coins, 2 is the default weight of a genuine coin
    coins = [2] * N
    # randomly select an index within the array to place a fake coin with a weight of either 1 (light) or 3 (heavy)
    fake_coin_index = random.randint(0, N - 1)
    coins[fake_coin_index] = random.choice((1,3))
    return coins

# function that weighs two piles of coins. Returns "left" to indicate left is heavier, "right" to indicate right is heavier, or "balanced" to indicate both sides weigh the same.
def scale(left, right):
    # every time this function is called it will increase the global weigh variable by 1
    global weighings
    weighings += 1
    # sum the weight of each pile of coins
    left_side = sum(left)
    right_side = sum(right)
    # weighing can have three outcomes, left is heavier, right is heavier, or balanced
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
    global weighings
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
                if(len(coin_pile) == 4):
                    special_case = (A[0] == B[0])
                    weighings += 1
                    if(special_case):
                        genuine_coin = [A[0]]
                    else:
                        genuine_coin = [A[1]]
                else:           
                    genuine_coin.append(C[0])
            fake_coin = divide_and_conquer_phase_2(B, A)
        # else if A < B then enter phase 2 with B being the heavy set of coins
        elif result == "right":
            if not genuine_coin:
                if(len(coin_pile) == 4):
                    special_case = (A[0] == B[0])
                    weighings += 1
                    if(special_case):
                        genuine_coin = [A[0]]
                    else:
                        genuine_coin = [A[1]]
                else:           
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

# print result function
def print_results(fake_coin, time):
    if fake_coin[0] < 2:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin[0]} gram. Took {weighings} weighs.")
    else:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin[0]} grams. Took {weighings} weighs.")

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

# function that runs a simulation
def simulation(count):
    # variables
    increment_by = 2048
    global weighings
    # start the similation for brute force
    # run the simulation 5 times at N coins, record time
    # increment N by 2048 ten times, run simualtion 5 times at each iteration, record time at each iteration
    print("\nEXECUTING BRUTE FORCE ALGORITHM...\n")
    for i in range(10):
        # increment number of coins for the next pile
        number_of_coins = count + increment_by * i
        print(f"Pile {i + 1} with {number_of_coins} coins had a result of: ")
        for j in range(5):
            # reset the weigh counter so each pile is counted independently
            weighings = 0
            coin_pile = initialize_coins(number_of_coins)
            result, time = stopwatch(brute_force, coin_pile)
            print_results(result, time)

    # repeat above process for divide and conquer
    print("\nEXECUTING DIVIDE AND CONQUER ALGORITHM...\n")
    for i in range(10):
        # increment number of coins for the next pile
        number_of_coins = count + increment_by * i
        print(f"Pile {i + 1} with {number_of_coins} coins had a result of: ")
        for j in range(5):
            # reset the weigh counter so each pile is counted independently
            weighings = 0
            coin_pile = initialize_coins(number_of_coins)
            result, time = stopwatch(divide_and_conquer, coin_pile)        
            print_results(result, time)
    return

# function that times a simulation
def stopwatch(algorithm, coins):
    start = time.perf_counter_ns()
    result = algorithm(coins)
    elapsed = time.perf_counter_ns() - start
    return result, elapsed

# function responsible for graphing the results, finding hidden constants, and displaying all of the gathered evidence
def graph_results():
    return

######################################################################################################################################################
######################################################################################################################################################
# redesigned functions to implement optimized design for speed

# this function intializes a pile of N coins with one fake coin (either light or heavy). It also precomputes an array of summed weights of contiguous coins
def initialize_coins_new(N):
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

# function that weighs two piles of coins. Returns "left" to indicate left is heavier, "right" to indicate right is heavier, or "balanced" to indicate both sides weigh the same.
def scale_new(prefix, left, right):
    # every time this function is called it will increase the global weigh variable by 1
    global weighings
    weighings += 1
    # look up the weight of each pile of coins using the prefix array, O(1) operation
    left_side = prefix[left[1]] - prefix[left[0]]
    right_side = prefix[right[1]] - prefix[right[0]] 
    # weighing can have three outcomes, left is heavier, right is heavier, or balanced
    if left_side > right_side:
        return "left"
    elif right_side > left_side:
        return "right"
    elif left_side == right_side:
        return "balanced"

# optimized algorithm that preforms the least amount of weighings to find the fake coin.
def divide_and_conquer_new(prefix, coins):
    global genuine_coin_new
    genuine_coin_new = None
    # call phase 1, phase 1 will call phase 2 if neccessary
    start = 0
    end = len(coins)
    fake_coin = divide_and_conquer_phase_1_new(prefix, start, end)
    # return fake coin    
    return fake_coin

# phase one of the optimized algorithm
def divide_and_conquer_phase_1_new(prefix, start, end):
    global genuine_coin_new
    global weighings
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
        result = scale_new(prefix, A, B)
        if result == "balanced":
            if genuine_coin_new is None:
                genuine_coin_new = start
            fake_coin = divide_and_conquer_phase_1_new(prefix, offset_2, end)
        # else if A > B then enter phase 2 with A being the heavy set of coins
        elif result == "left":
            if genuine_coin_new is None:
                if(end - offset_2 == 0):
                    special_case = (prefix[start + 1]) == (prefix[start + 2] - prefix[start + 1])
                    weighings += 1
                    if(special_case):
                        genuine_coin_new = start
                    else:
                        genuine_coin_new = offset_1
                else:    
                    genuine_coin_new = offset_2
            fake_coin = divide_and_conquer_phase_2_new(prefix, B, A)
        # else if A < B then enter phase 2 with B being the heavy set of coins
        elif result == "right":
            if genuine_coin_new is None:
                if(end - offset_2 == 0):
                    special_case = (prefix[start + 1]) == (prefix[start + 2] - prefix[start + 1])
                    weighings += 1
                    if(special_case):
                        genuine_coin_new = start
                    else:
                        genuine_coin_new = offset_1
                else:    
                    genuine_coin_new = offset_2
            fake_coin = divide_and_conquer_phase_2_new(prefix, A, B)
    # found the fake coin in phase 2
    return fake_coin

# phase two of the optimized algorithm
def divide_and_conquer_phase_2_new(prefix, L, H):
    # base case, if light and heavy groups are only 1 coin each, then fake coin is either in L or H
    if (L[1] - L[0]) == 1 and (H[1] - H[0]) == 1:
        global weighings
        weighings +=1
        result = ((prefix[genuine_coin_new + 1] - prefix[genuine_coin_new]) == (prefix[L[1]] - prefix[L[0]]))
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
        result = scale_phase2_new(prefix, L1, H1, L2, H2)
        if result == "balanced":
            fake_coin = divide_and_conquer_phase_2_new(prefix, L3, H3)
        elif result == "left":
            fake_coin = divide_and_conquer_phase_2_new(prefix, L2, H1)
        elif result == "right":
            fake_coin = divide_and_conquer_phase_2_new(prefix, L1, H2)
    return fake_coin

# new scale method for phase 2
def scale_phase2_new(prefix, L1, H1, L2, H2):
    global weighings
    weighings += 1
    left_pan = (prefix[L1[1]] - prefix[L1[0]]) + (prefix[H1[1]] - prefix[H1[0]])
    right_pan = (prefix[L2[1]] - prefix[L2[0]]) + (prefix[H2[1]] - prefix[H2[0]])
    
    if left_pan > right_pan:
        return "left"
    elif left_pan < right_pan:
        return "right"
    else:
        return "balanced"


def print_results_new(prefix, fake_coin, time):
    fake_coin_weight = prefix[fake_coin + 1] - prefix[fake_coin]
    if fake_coin_weight < 2:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin_weight} gram. Took {weighings} weighs.")
    else:
        print(f"Fake coin found in {time}ns! Coin weighs {fake_coin_weight} grams. Took {weighings} weighs.")
    return

def stopwatch_new(prefix, algorithm, coins):
    start = time.perf_counter_ns()
    result = algorithm(prefix, coins)
    elapsed = time.perf_counter_ns() - start
    return result, elapsed

def simulation_new(count):
    # variables
    increment_by = 2048
    global weighings
    # start the similation for brute force
    # run the simulation 5 times at N coins, record time
    # increment N by 2048 ten times, run simualtion 5 times at each iteration, record time at each iteration
    print("\nEXECUTING BRUTE FORCE ALGORITHM...\n")
    for i in range(10):
        # increment number of coins for the next pile
        number_of_coins = count + increment_by * i
        print(f"Pile {i + 1} with {number_of_coins} coins had a result of: ")
        for j in range(5):
            # reset the weigh counter so each pile is counted independently
            weighings = 0
            prefix, coin_pile = initialize_coins_new(number_of_coins)
            result, time = stopwatch_new(prefix, brute_force_new, coin_pile)
            print_results_new(prefix, result, time)

    # repeat above process for divide and conquer
    print("\nEXECUTING DIVIDE AND CONQUER ALGORITHM...\n")
    for i in range(10):
        # increment number of coins for the next pile
        number_of_coins = count + increment_by * i
        print(f"Pile {i + 1} with {number_of_coins} coins had a result of: ")
        for j in range(5):
            # reset the weigh counter so each pile is counted independently
            weighings = 0
            prefix, coin_pile = initialize_coins_new(number_of_coins)
            result, time = stopwatch_new(prefix, divide_and_conquer_new, coin_pile)        
            print_results_new(prefix, result, time)
    return

def brute_force_new(prefix, coins):
    global genuine_coin_new
    genuine_coin_new = None
    number_of_coins = len(coins)
    for i in range(0, number_of_coins, 2):
        left_coin = (i, i + 1)
        right_coin = (i + 1, i + 2)
        result = scale_new(prefix, left_coin, right_coin)
        if(result == "balanced"):
            if(genuine_coin_new == None):
                genuine_coin_new = left_coin
            if(i + 2 >= number_of_coins - 1):
                fake_coin = right_coin[1]
                break
        else:
            if(i == 0):
                genuine_coin_new = (right_coin[0] + 1, right_coin[1] + 1)
            result = scale_new(prefix, genuine_coin_new, left_coin)
            if(result == "balanced"):
                fake_coin = right_coin[0]
                break
            else:
                fake_coin = left_coin[0]
                break

    return fake_coin

######################################################################################################################################################
######################################################################################################################################################

# main executable function
def main():
    N = get_user_input()
    # program using old functions O(n) ceiling on D&C because of inefficient old scale method
    simulation(N)
    # program using new functions to acheive O(log_3(n)) on D&C
    simulation_new(N)

# control mechanism to execute main
if __name__ == "__main__":
    main()