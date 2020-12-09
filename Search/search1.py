# Index search algorithm
def search(items, target):
  try:
    return items.index(target)
  except ValueError:
    return -1

# Notes:
# Uses python's built-in list index function to search for target
#
# Performance:
# Time is: 4.0531158447265625e-06   Last item in list
# Time is: 7.152557373046875e-07    Middle item in list
# Time is: 7.152557373046875e-07    Item near the front