"""
86 Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        helper = ListNode(0)
        helper.next = head

        # Find the first node whose value >= x. "right" will stop on this node
        left, right = helper, head
        while right and right.val < x:
            left = right
            right = right.next

        if not right:
            return head

        # Now right's value is x, and left is the node "pre" right.
        # "left" will link to the next available node whose value is smaller than x. "right" will be the new head of the right part
        # After traversing all nodes, we need to relink "left" and "right"
        pre, node = right, right.next
        while node:
            if node.val < x:    # put node to left because it is less than x
                # link node to left part
                left.next = node
                left = node
                # process the right part
                pre.next = node.next
            else:
                pre = node
            node = node.next
        
        # relink the left and right
        left.next = right

        return helper.next

obj = Solution()
l1 = ListNode(0)
l1.fromList([6,4,3,2,5,2])
l2 = obj.partition(l1,3)
PrintLinkedList(l2)