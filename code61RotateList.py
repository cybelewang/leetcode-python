from ListNode import *
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next:
            return head

        pre = ListNode(0)
        pre.next = head

        tail, l = head, 0
        while not tail and l <= k:
            l += 1
            tail = tail.next
        
        if not tail:
            k = k % l
            tail = head
            for i in range(k):
                tail = tail.next
        
        while not tail.next:
            head = head.next
            tail = tail.next

        tail.next = pre.next
        pre.next = head.next
        head.next = None

        return pre.next

        


