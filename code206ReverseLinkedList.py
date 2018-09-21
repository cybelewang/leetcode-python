"""
206 Reverse Linked List

Reverse a singly linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        while head:
            node = head.next
            head.next = pre.next
            pre.next = head
            head = node
        
        return pre.next
