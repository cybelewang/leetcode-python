from ListNode import *
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# similar to merge sort, starting from sorting every two nodes, then every four node, then every 8 nodes... until 2^m >= n
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        node, n = head, 0
        while node:
            node = node.next
            n += 1

        pre = ListNode(0)
        pre.next = head

        period = 2
        while period < n:
            
            period *= 2

        return pre.next