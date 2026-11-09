# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

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
