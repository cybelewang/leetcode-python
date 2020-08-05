"""
381 Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""
# same as 380, but using a list to keep track of the index
from random import choice
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.data = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            self.map[val].add(len(self.data))
            self.data.append(val)
            return False
        else:
            self.map[val] = {len(self.data), }
            self.data.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            # randomly select a position for val in self.data
            pos = self.map[val].pop()   
            # assign pos with last_data
            last_data = self.data[-1]
            self.data[pos] = last_data
            if pos != len(self.data) - 1:   # trap here! if pos is len(data) - 1, then we removed len(data) - 1 twice! So we need to exclude this condition
                # first remove the original index (len(self.data)-1) for last_data
                self.map[last_data].remove(len(self.data)-1)
                # then assign the new index (pos) for last_data
                self.map[last_data].add(pos)
            # remove last data
            self.data.pop()

            if not self.map[val]:
                self.map.pop(val)
            
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.data)


obj = RandomizedCollection()
print(obj.insert(4))
print(obj.insert(3))
print(obj.insert(4))
print(obj.insert(2))
print(obj.remove(4))
print(obj.remove(3))
print(obj.remove(4))
print(obj.remove(4))

"""
["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
[[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]
"""
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()