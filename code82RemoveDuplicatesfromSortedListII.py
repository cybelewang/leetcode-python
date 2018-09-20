"""
82 Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# The basic idea is to use a temporary node to save the "candidate" ListNode on the first time seeing a different value. 
# Then we set this temporary node to None if duplicated num is seen. The next time we see a different value node, we will check this temporary node, if it is not None, we will link it.
from ListNode import *
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head

        pre = ListNode(0)
        pre.next = head

        num = head.val
        left, right, node = pre, head.next, head    # node is the candidate ListNode to be linked to left
        while right:
            if right.val == num:
                node = None
            else:
                if node:
                    left.next = node
                    left = left.next

                node = right
                num = right.val
            
            right = right.next
        
        if node:    # bug fixed here: forgot the remaining node when "while" loop ends
            left.next = node
            node.next = None
        else:
            left.next = None

        return pre.next

obj = Solution()
l1 = ListNode(0)
l1.fromList([1,1,2,2,3])
l2 = obj.deleteDuplicates(l1)
PrintLinkedList(l2)