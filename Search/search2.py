# Linear search algorithm
def search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    # Did not find the item
    return -1

# Notes:
# Traverses through list until it finds the target or reaches the end without finding it.
# This algorithm is n time.
#
# range() expression creates a list of indexes that is same size as list being search,
#   leading to a large memory footprint
# xrange() expression is better but not advised for newer code
#
# Performance:
# Time is: 0.04465222358703613      Last item in list
# Time is: 0.023434162139892578     Middle item in list
# Time is: 3.5762786865234375e-06   Item near the front