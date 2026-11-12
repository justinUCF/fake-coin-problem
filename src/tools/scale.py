# FAKE COIN PROBLEM
# AUTHORS: Giorgio Miguel Torregrosa and Justin Gamboa

# global variables
weighings = 0

# function that weighs two piles of coins. Returns "left" to indicate left is heavier, "right" to indicate right is heavier, or "balanced" to indicate both sides weigh the same.
def scale(prefix, left, right):
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

# scale method used for phase 2
def scale_phase2(prefix, L1, H1, L2, H2):
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
