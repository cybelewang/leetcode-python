"""
2 Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

from ListNode import *

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carrier = 0 # carrier
        head = node = ListNode(0) # head of the result linked list
        while l1 or l2 or carrier:
            num1 = num2 = 0
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            (carrier, val) = divmod(num1 + num2 + carrier, 10)
            node.next = ListNode(val)
            node = node.next
        return head.next