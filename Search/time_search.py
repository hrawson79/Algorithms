# Timing search algorithms from other files
import time
# Uncomment for algorithm using built-in indexing
#from search1 import search
# Uncomment for algorithm using linear search
#from search2 import search
# Uncomment for algorithm using binary search
from bsearch import search

# Create a large list
items = range(1000000)

# Clock the start time
start = time.time()
search(items, 999999)  # Look for the last item
# Clock the stop time
stop = time.time()
print("Time is: " + str(stop-start))

# Clock the start time
start = time.time()
search(items, 499999)  # Look for the middle item
# Clock the stop time
stop = time.time()
print("Time is: " + str(stop-start))

# Clock the start time
start = time.time()
search(items, 10)  # Look for an item near the front
# Clock the stop time
stop = time.time()
print("Time is: " + str(stop-start))