from ListNode import *
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head

        left, right = head, head.next
        num = head.val

        while right:
            if right.val != num:
                num = right.val
                left.next = right
                left = left.next
            
            right = right.next
        
        # Terminate the tail of the new linked list
        left.next = None

        return head

obj = Solution()
l1 = ListNode(0)
l1.fromList([1,1,1,1,1,2,2,2,2])
l2 = obj.deleteDuplicates(l1)
PrintLinkedList(l2)