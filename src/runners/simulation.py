# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import time
from tools import scale
from tools.coins import initialize_coins
from tools.results import print_results
from brute_force.brute_force import brute_force
from divide_and_conquer.divide_and_conquer import divide_and_conquer

# 2D arrays to hold times. Every simulation will iterate 10 times with 5 runs each iteration
brute_force_times = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
divide_and_conquer_times = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

# runs a simulation to gather times for each algorithm
def simulation(count):
    # constant variables
    INCREMENT_COUNT = 2048
    SIMULATION_ITERATIONS = 10
    SIMULATION_RUNS = 5
    # start the similation for brute force
    # run the simulation 5 times at N coins, record time
    # increment N by 2048 ten times, run simualtion 5 times at each iteration, record time at each iteration
    print("\nEXECUTING BRUTE FORCE ALGORITHM...\n")
    for i in range(SIMULATION_ITERATIONS):
        # increment number of coins for the next pile
        number_of_coins = count + INCREMENT_COUNT * i
        for j in range(SIMULATION_RUNS):
            # reset the weigh counter so each pile is counted independently
            scale.weighings = 0
            prefix, coin_pile = initialize_coins(number_of_coins)
            result, elapsed = stopwatch(prefix, brute_force, coin_pile)
            brute_force_times[i][j] = elapsed
    print_brute_force_times(SIMULATION_ITERATIONS, SIMULATION_RUNS)
    # repeat above process for divide and conquer
    print("\nEXECUTING DIVIDE AND CONQUER ALGORITHM...\n")
    for i in range(SIMULATION_ITERATIONS):
        # increment number of coins for the next pile
        number_of_coins = count + INCREMENT_COUNT * i
        for j in range(SIMULATION_RUNS):
            # reset the weigh counter so each pile is counted independently
            scale.weighings = 0
            prefix, coin_pile = initialize_coins(number_of_coins)
            result, elapsed = stopwatch(prefix, divide_and_conquer, coin_pile)
            divide_and_conquer_times[i][j] = elapsed
    print_divide_and_conquer_times(SIMULATION_ITERATIONS, SIMULATION_RUNS)

# timing method used to time a given algorithm with specified number of coins
def stopwatch(prefix, algorithm, coins):
    start = time.perf_counter_ns()
    result = algorithm(prefix, coins)
    elapsed = time.perf_counter_ns() - start
    return result, elapsed

# use to test algortithms after making significant algorithms changes
def debug_algorithms(N, increment, iterations, runs):
    """
    Debug algorithms parameters: (number of coins, increment coins by, how many times to add increment, how many times to run at each coin count)
    """
    # constant variables
    INCREMENT_COUNT = increment
    SIMULATION_ITERATIONS = iterations
    SIMULATION_RUNS = runs
    count = N
    # start the similation for brute force
    # run the simulation 5 times at N coins, record time
    # increment N by 2048 ten times, run simualtion 5 times at each iteration, record time at each iteration
    print("\nDEBUGGING BRUTE FORCE ALGORITHM...\n")
    for i in range(SIMULATION_ITERATIONS):
        # increment number of coins for the next pile
        number_of_coins = count + INCREMENT_COUNT * i
        print(f"Pile {i + 1} with {number_of_coins} coins had a result of: ")
        for j in range(SIMULATION_RUNS):
            # reset the weigh counter so each pile is counted independently
            scale.weighings = 0
            prefix, coin_pile = initialize_coins(number_of_coins)
            result, elapsed = stopwatch(prefix, brute_force, coin_pile)
            print_results(prefix, result, elapsed, number_of_coins)
    # repeat above process for divide and conquer
    print("\nDEBUGGING DIVIDE AND CONQUER ALGORITHM...\n")
    for i in range(SIMULATION_ITERATIONS):
        # increment number of coins for the next pile
        number_of_coins = count + INCREMENT_COUNT * i
        print(f"Pile {i + 1} with {number_of_coins} coins had a result of: ")
        for j in range(SIMULATION_RUNS):
            # reset the weigh counter so each pile is counted independently
            scale.weighings = 0
            prefix, coin_pile = initialize_coins(number_of_coins)
            result, elapsed = stopwatch(prefix, divide_and_conquer, coin_pile)
            print_results(prefix, result, elapsed, number_of_coins)

# method used to print run times for brute force
def print_brute_force_times(SIMULATION_ITERATIONS, SIMULATION_RUNS):
    global brute_force_times
    for i in range(SIMULATION_ITERATIONS):
        print(f"Simulation Iteration {i + 1}: ", end="")
        for j in range(SIMULATION_RUNS):
            print(f"{brute_force_times[i][j]} ", end="")
        print()
    return

# method used to print run times for divide and conquer
def print_divide_and_conquer_times(SIMULATION_ITERATIONS, SIMULATION_RUNS):
    global brute_force_times
    for i in range(SIMULATION_ITERATIONS):
        print(f"Simulation Iteration {i + 1}: ", end="")
        for j in range(SIMULATION_RUNS):
            print(f"{divide_and_conquer_times[i][j]} ", end="")
        print()
    return
