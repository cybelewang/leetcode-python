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

    # 8/4/2020
    # O(N) time, O(N) space solution
    # use dict's setdefault method to simplify code
    def copyRandomList2(self, head: 'Node') -> 'Node':
        src_dst = {}
        sentinel = Node(0)
        src, pre = head, sentinel
        while src:
            dst = src_dst.setdefault(src, Node(src.val))
            pre.next = dst
            pre = dst
            if src.random:
                dst.random = src_dst.setdefault(src.random, Node(src.random.val))
            src = src.next
        
        return sentinel.next

    # 8/4/2020
    # O(N) time, O(1) space solution
    def copyRandomList3(self, head: 'Node') -> 'Node':
        # step 1: copy node after origin nodes
        cur = head
        while cur:
            temp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = temp
            cur = temp
        # step 2: link copied nodes' random nodes
        cur = head
        while cur:
            clone = cur.next
            if cur.random:
                clone.random = cur.random.next
            cur = cur.next.next
            
        # step 3: separate copied nodes from original linked list
        sentinel = Node(0)
        cur, pre = head, sentinel
        while cur:
            pre.next = cur.next
            cur.next = cur.next.next
            cur = cur.next
            pre = pre.next
        
        return sentinel.next
            