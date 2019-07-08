"""
138 Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        copy = RandomListNode(head.label) # copy
        res = copy

        origin = head
        link = {origin: copy, None:None}

        while origin:
            # copy "next"
            if origin.next in link:
                copy.next = link[origin.next]
            else:
                new_node = RandomListNode(origin.next.label)
                copy.next = new_node
                link[origin.next] = new_node

            # copy "random"
            if origin.random in link:
                copy.random = link[origin.random]
            else:
                new_node = RandomListNode(origin.random.label)
                copy.random = new_node
                link[origin.random] = new_node

            # advance iterators
            origin = origin.next
            copy = copy.next
        
        return res