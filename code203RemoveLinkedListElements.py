"""
203 Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head

        left, right = pre, head
        while right:
            if right.val != val:
                left.next = right
                left = right
            right = right.next
        
        left.next = None
        return pre.next

obj = Solution()
test_case = [1, 1]
l1 = ListNode(0)
l1.fromList(test_case)
l1.printAll()
print()
l2 = obj.removeElements(l1, 1)
l2.printAll()