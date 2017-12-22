"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
# What about capacity is 0 ? 1?
# use a double linked list to store node (key, value), and a map to get the node from the key
# definition of the double linked list node
class ListNode(object):
    
    def __init__(self, x):
        """
        :type x: tuple
        we need tuple because 
        """
        self.val = x
        self.prev = None
        self.next = None

# definition of the double linked list
class DoubleLinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def appendHead(self, node):
        """
        append node to head
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        node.next = self.head   # connect node to the head

        if self.head is None:
            self.tail = node    # don't forget to update tail if this is the first node in the linked list
        else:
            self.head.prev = node
        self.head = node

    def append(self, node):
        """
        append node to tail
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        node.prev = self.tail    # connect node to the tail

        if self.tail is None:
            self.head = node    # don't forget to update head if this is the first node in the linked list
        else:
            self.tail.next = node

        self.tail = node

    def remove(self, node):
        """
        remove a node from the linked list
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        # save the prev and next for node
        prev = node.prev
        next = node.next

        # disconnect node
        node.prev = None
        node.next = None

        # process the left to right link
        if prev is None:
            self.head = next
        else:
            prev.next = next

        # process the right to left link
        if next is None:
            self.tail = prev
        else:
            next.prev = prev

        """ following is the original version with bugs fixed
        if self.head == node:
            # remove a head node
            self.head = node.next
            if self.head is not None:   # bug fixed: forgot to disconnect the head with removed node
                self.head.prev = None
            node.next = None
        elif self.tail == node:
            # remove a tail node
            self.tail = node.prev
            if self.tail is not None:   # bug fixed: forgot to disconnect the tail with removed node
                self.tail.next = None
            node.prev = None
        else:
            # remove a middle node
            node.prev.next = node.next
            if node.next is not None:   # bug fixed: forgot to connect the next node's prev with previous node
                node.next.prev = node.prev
            node.prev = None
            node.next = None
        """

class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        if capacity < 1:
            raise ValueError

        self.capacity = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            # move node to list head (most recently used)
            self.list.remove(node)
            self.list.appendHead(node)
            return node.val[1]
        else:
            return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            # key is already in cache
            node = self.cache[key]
            # update the value
            node.val = (key, value)
            # move node to head (most recently used)
            self.list.remove(node)
            self.list.appendHead(node)
        else:
            # check if cache size exceeds limit before putting the new node
            if len(self.cache) == self.capacity:
                # size exceeding limit, need to remove the least recently used node
                tail = self.list.tail
                self.list.remove(tail)
                self.cache.pop(tail.val[0])
            
            # create a new node and put into cache    
            node = ListNode((key, value))
            self.cache[key] = node
            self.list.appendHead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(3)

cache.put(1, 1) # LRU: [1]
cache.put(2, 2) # LRU: [2, 1]
cache.put(3, 3) # LRU: [3, 2, 1]
cache.put(4, 4)           # evicts key 1, LRU: [4, 3, 2]
print(cache.get(4))       # returns 4, LRU: [4, 3, 2]
print(cache.get(3))       # returns 3, LRU: [3, 4, 2]
print(cache.get(2))       # returns 2, LRU: [2, 3, 4]
print(cache.get(1))       # returns 2, LRU: [2, 3, 4]
cache.put(5,5)            # evicts key 4, LRU: [5, 2, 3]
print(cache.get(1))       # returns -1
print(cache.get(2))       # returns 2
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns -1
print(cache.get(5))       # returns 5

"""
Input:
["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
[[3],       [1,1],[2,2],[3,3],[4,4],[4],   [3],  [2],  [1], [5,5], [1],  [2],  [3],  [4],  [5]]
Output:
[null,null,null,null,null,4,3,2,-1,null,-1,2,-1,4,5]
Expected:
[null,null,null,null,null,4,3,2,-1,null,-1,2,3,-1,5]
"""