# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
from tools.user_input import get_user_input
from tools.old.simulation import simulation

# main executable function
def main():
    # program using old functions O(n) ceiling on D&C because of inefficient old scale method
    simulation(get_user_input())

    # program using new functions to acheive O(log_3(n)) on D&C
    # simulation_new(get_user_input())

# control mechanism to execute main
if __name__ == "__main__":
    main()
