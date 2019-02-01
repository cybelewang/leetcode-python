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
    # use a dummy node
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

    # 2nd round solution on 2/1/2019, without using a dummy node
    def reverseList2(self, head):
        node, head = head, None
        while node:
            _next = node.next
            node.next = head
            head = node
            node = _next
        
        return head