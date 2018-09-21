"""
160 Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution(object):

    # OJ best solution
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointer_a, pointer_b = headA, headB
        
        while pointer_a is not pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next
        return pointer_a

    # my solution: get length difference, then align pointers
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        # get A, B length
        a, b = headA, headB
        cntA, cntB = 1, 1
        while a.next:
            cntA += 1
            a = a.next
        
        while b.next:
            cntB += 1
            b = b.next
        
        # make A's length < B's length
        if cntA > cntB:
            cntA, cntB = cntB, cntA
            headA, headB = headB, headA
        
        # align the two pointers
        a, b = headA, headB
        for i in range(cntB - cntA):
            b = b.next
        
        # now start moving both pointers
        while a and b and a!=b:
            a = a.next
            b = b.next
        
        return a