"""
460 LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. 
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. 
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
# similar to 146 LRU Cache, All O1 Data Structure
from DoubleLinkedList import *
class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}   # map from key to a double linked list node, whose value is a list [key, value, frequency node in self.freqlist]
        self.freqlist = DoubleLinkedList() # a double linked list with each node holding a list [frequency, double linked list with nodes (self.map's values) of this frequency]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            print('-1')
            return -1
        else:
            # get the corresponding ListNode
            node = self.map[key]

            # update this node's frequency
            self._updatefreq(node)
            print(node.val[1])
            return node.val[1]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity < 1: #bug fixed: corner case when capacity is 0
            return

        if key in self.map:
            # get the corresponding ListNode
            node = self.map[key]

            # update the value
            node.val[1] = value
        else:            
            if len(self.map) == self.capacity:
                # evict the least used key
                self._evict()
            # create a new ListNode
            node = ListNode([key, value, None])
            # add key and value into self.map
            self.map[key] = node

        # update this node's frequency
        self._updatefreq(node)


    def _evict(self):
        """
        evict the least used node
        rtype: void
        """
        # get the frequency ListNode with the least frequency
        least_freq_node = self.freqlist.tail
        # get the least frequency list
        least_freq_list = least_freq_node.val[1]

        # get the tail node in the least frequency list
        tail = least_freq_list.tail
        # get the key value
        key = tail.val[0]

        # remove tail node from the least frequency list
        least_freq_list.remove(tail)
        # remove the least frequency node, if its list is empty
        if least_freq_list.isempty():
            self.freqlist.remove(least_freq_node)

        # remove key from self.map
        self.map.pop(key)


    def _updatefreq(self, node):
        """
        update frequency of a node
        :type: node: ListNode
        :rtype: void
        """
        if node is None:
            return

        # get key, value and corresponding frequency ListNode
        old_freq_node = node.val[2]

        if old_freq_node is None:
            # this is a new node
            if self.freqlist.tail is None or self.freqlist.tail.val[0] != 1:
                new_freq_node = ListNode([1, DoubleLinkedList()])
                self.freqlist.append(new_freq_node)
            else:
                new_freq_node = self.freqlist.tail
            
            # get the new frequency list
            new_freq_list = new_freq_node.val[1]

            # append node to the head of new frequency list so it is the most recently used node
            new_freq_list.append_head(node)

            # update the node's frequency ListNode from old one to new one
            node.val[2] = new_freq_node

            return


        # get the current frequency and the linked list of nodes with the same frequency
        old_freq, old_freq_list = old_freq_node.val

        # remove node from the old frequency's list
        old_freq_list.remove(node)

        # increase frequency by 1
        new_freq = old_freq + 1

        # check if the higher frequency node exists and equal to new frequency
        if old_freq_node.prev is None or old_freq_node.prev.val[0] != new_freq:
            # frequency (freq + 1) node doesn't exist, create one
            new_freq_node = ListNode([new_freq, DoubleLinkedList()])
            # insert the newly created frequency node into self.freqlist
            self.freqlist.insert_before(old_freq_node, new_freq_node)
        else:
            # frequency (freq + 1) node exists
            new_freq_node = old_freq_node.prev

        # get the new frequency list
        new_freq_list = new_freq_node.val[1]

        # append node to the head of new frequency list so it is the most recently used node
        new_freq_list.append_head(node)

        # update the node's frequency ListNode from old one to new one
        node.val[2] = new_freq_node

        # remove the old frequency node, if its list is empty
        if old_freq_list.isempty():
            self.freqlist.remove(old_freq_node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       #// returns 1
cache.put(3, 3)    #// evicts key 2
cache.get(2)       #// returns -1 (not found)
cache.get(3)       #// returns 3.
cache.put(4, 4)    #// evicts key 1.
cache.get(1)       #// returns -1 (not found)
cache.get(3)       #// returns 3
cache.get(4)       #// returns 4