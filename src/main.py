# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# imports
import argparse
from tools.user_input import get_user_input
from runners.simulation import simulation

# main executable function
def main():
    parser = argparse.ArgumentParser(description="The Fake Coin Problem")
    parser.add_argument("--mode","-m", choices=["simulation"], default="simulation", help="Select the mode to run (default: simulation)")
    args = parser.parse_args()

    if args.mode == "simulation":
        simulation(get_user_input())

# control mechanism to execute main
if __name__ == "__main__":
    main()
