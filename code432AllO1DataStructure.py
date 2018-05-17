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
        self.strcnt = defaultdict(int)
        self.cntstrs = defaultdict(set)
        self.min = 0
        self.max = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        cnt = self.strcnt[key]  # get original count
        if cnt > 0:
            self.cntstrs[cnt].discard(key)  # remove from original count-set(str) dict

        cnt += 1    # increase count
        self.strcnt[key] += 1   # update count for key

        self.cntstrs[cnt].add(key)  # add key into new count's dict
        self.max = max(self.max, cnt)   # update max count of the whole class

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        cnt = self.strcnt[key]  # get original count
        if cnt > 0:
            self.cntstrs[cnt].discard(key)  # remove from original count-set(str) dict

            cnt -= 1    # decrease count
            self.strcnt[key] -= 1   # update count for key

            if cnt > 0:
                self.cntstrs[cnt].add(key)  # add key into new count's dict
                self.min = max(self.min, cnt)   # update min count of the whole class

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        keys = self.cntstrs[self.max]
        if keys:
            res = keys.pop()
            keys.add(res)
            return res
        else:
            return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        keys = self.cntstrs[self.min]
        if keys:
            res = keys.pop()
            keys.add(res)
            return res
        else:
            return ''




# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()