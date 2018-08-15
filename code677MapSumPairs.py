"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. 
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""
class TrieNode:
    
    def __init__(self, c, v):
        self.char = c
        self.val = v
        self.children = {}

# my own solution with bugs fixed
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.root = TrieNode('', 0)
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.map:
            val -= self.map[key]
            self.map[key] += val    # bug fixed: forgot to update self.map[key]
        else:
            self.map[key] = val     # # bug fixed: forgot to add key val into self.map

        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode(c, 0)
            
            node = node.children[c]               
            node.val += val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        
        return node.val         

obj = MapSum()
obj.insert("apple", 3)
print(obj.sum('ap'))    # expected 3
obj.insert('app', 2)
print(obj.sum('ap'))    # expected 5
obj.insert("apple", 4)
print(obj.sum('ap'))    # expected 6
print(obj.sum('b'))    # expected 0
print(obj.sum('apple'))    # expected 4
print(obj.sum('appled'))    # expected 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)