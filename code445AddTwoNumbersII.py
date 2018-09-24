"""
445 Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getLength(head):
            """
            get the length of the linked list
            """
            count = 0
            while head:
                count += 1
                head = head.next

            return count

        def reverse(head):
            """
            reverse the linked list in place
            """
            cur, pre = head, None
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            return pre            

        len1, len2 = getLength(l1), getLength(l2)
        if len2 > len1:
            l1, l2 = l2, l1
            len1, len2 = len2, len1
        
        helper = ListNode(0)
        it = helper
        for _ in range(len1-len2):
            it.next = ListNode(l1.val)
            l1 = l1.next
            it = it.next
        
        for _ in range(len2):
            it.next = ListNode(l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
            it = it.next
        
        head = reverse(helper.next)
        node, carry = head, 0
        while node:
            temp = carry
            carry = (node.val + carry)//10
            node.val = (node.val + temp)%10 # bug fixed: cannot use updated carry to calculate the remain value, must save carry first to "temp"
            node = node.next
        
        head = reverse(head)
        if carry > 0:
            helper.val = carry
            helper.next = head
            return helper
        else:
            return head

l1, l2 = ListNode(0), ListNode(0)
l1.fromList([9, 9, 9, 9])
l2.fromList([1])
PrintLinkedList(l1)
PrintLinkedList(l2)
l3 = Solution().addTwoNumbers(l2, l1)
PrintLinkedList(l3)
