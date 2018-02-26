"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Copy the rest of the nodes
from ListNode import *
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre = None
        while node.next is not None:
            pre = node
            node.val = node.next.val
            node = node.next
        pre.next = None

head = ListNode(0)
head.next = ListNode(1)
PrintLinkedList(head)

obj = Solution()
obj.deleteNode(head)
PrintLinkedList(head)