# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# TODO: use a dictionary to count each element
# fruitCounter = dict()
# fruitCounter = defaultdict(int)
# define owned factory method // initial value
fruitCounter = defaultdict(lambda: 100)
# %% defaultdict(): any key you didn't explicitly add to the dictionary
# will be assigned a default value when you try to access it.

# TODO: Count the elements in the list
# : error with default dict()
# for fruit in fruits:
#     fruitCounter[fruit] = 1
###
# unnecessary visual noise to the code.
# for fruit in fruits:
#     if fruit in fruitCounter.keys():
#         fruitCounter[fruit] += 1
#     else:
#         fruitCounter[fruit] = 1
####
for fruit in fruits:
    fruitCounter[fruit] += 1

# TODO: print the result
print(fruitCounter)
