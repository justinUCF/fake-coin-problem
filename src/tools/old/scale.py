# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# global variables
weighings = 0

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
