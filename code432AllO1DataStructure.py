"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""

# use two dict, one from key to count, and the other one from count to a set of keys
from collections import defaultdict
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_value = defaultdict(int)   # map from key to its value
        self.value_keys = defaultdict(set)  # map from count to a set of keys with this value
        self.min = 0    # min value
        self.max = 0    # max value

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        value = self.key_value[key]  # get original value, if the key doesn't exist, value is 0
        keys = self.value_keys[value]  # get original set of keys corresponding to value, if the value doesn't exist, keys is empty set
        keys.discard(key)  # remove key from original value - key sets, if key exists in the set
        if not keys:
            self.value_keys.pop(value)
            """
            # What's wrong with the below code? think about after inc('a') twice, max and min are 2, and now inc('b'), min will not be updated to 1
            if self.min == value:
                self.min = value + 1
            """
        # increase value and update maps
        value += 1
        self.key_value[key] = value
        self.value_keys[value].add(key)
        # update max
        self.max = max(self.max, value)
        # update min
        self.min = 1 if self.min == 0 else min(self.min, value)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.key_value:
            return
        # get original value and key set
        value = self.key_value[key]
        keys = self.value_keys[value]
        keys.discard(key)
        if not keys:
            self.value_keys.pop(value)
            if self.max == value:
                self.max = value - 1

        # decrease value and update maps
        value -= 1
        if value > 0:
            self.key_value[key] = value
            self.value_keys[value].add(key)
        else:# bug fixed: forgot to pop key with value 0
            self.key_value.pop(key)

        # update min
        self.min = 1 if self.min == 0 else min(self.min, value)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.max == 0:
            return ''
        else:
            keys = self.value_keys[self.max]
            res = keys.pop()
            keys.add(res)
            return res

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.min == 0:
            return ''
        else:
            keys = self.value_keys[self.min]
            res = keys.pop()
            keys.add(res)
            return res

obj = AllOne()
print(obj.min)
print(obj.max)
obj.inc('a')
print(obj.min)
print(obj.max)
obj.dec('a')
print(obj.min)
print(obj.max)
obj.inc('a')
obj.inc('a')
obj.inc('b')
print(obj.min)
print(obj.max)
obj.dec('b')
obj.inc('c')
obj.inc('c')
obj.inc('c')
print(obj.min)
print(obj.max)
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()