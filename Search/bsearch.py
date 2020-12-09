# Binary search algorithm
def search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (high + low) // 2
        item = items[mid]
        if target == item:
            return mid
        elif target < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Notes:
# Divides the list of items in two each iteration.
# Algorithm is log2(n) time
# 
# Performance:
# Time is: 5.7220458984375e-06      Last item in list
# Time is: 9.5367431640625e-07      Middle item in list
# Time is: 4.5299530029296875e-06   Item near the front