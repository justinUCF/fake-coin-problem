# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import time
from tools.old import scale
from tools.old.coins import initialize_coins
from tools.old.results import print_results
from brute_force.old.brute_force import brute_force
from divide_and_conquer.old.divide_and_conquer import divide_and_conquer

# function that runs a simulation
def simulation(count):
    # variables
    increment_by = 2048
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
            scale.weighings = 0
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
            scale.weighings = 0
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
