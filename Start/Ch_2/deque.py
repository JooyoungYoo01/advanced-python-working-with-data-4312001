# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"Item Count: {len(d)}", "items in deck")

# TODO: deques can be iterated over
for elem in d:
    print(elem)
    print(elem.upper())
# TODO: manipulate items from either end
d.pop()         # erase "z"
d.popleft()     # erase "a"
d.append(2)     # append "2" in front
d.appendleft(1)  # append "1" in back
print(d)
# TODO: use an index to get a particular item
print(d)
d.rotate(1)
print(d)