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
        if k == 0 or not head or head.next is None:
            return head
        
        # helper node to handle the new head case
        pre = ListNode(0)
        pre.next = head

        tail, l = pre, 0
        while tail.next is not None and l < k: # When while condition fails, tail is either on "tail" node, or l == k, which means tail is on the ready to move position
            l += 1
            tail = tail.next
        
        if tail.next is None: # if tail is on "tail", this means k >= l, so we need to put the tail back on k%l position
            k = k % l
            tail = pre
            for i in range(k):
                tail = tail.next
        
        helper = pre
        while tail.next is not None: # After this, helper's next will point to the start node of the section to be rotated to the beginning
            helper = helper.next
            tail = tail.next

        tail.next = pre.next
        pre.next = helper.next
        helper.next = None

        return pre.next

obj = Solution()
l1 = ListNode(0)
l1.fromList([1, 2])
l2 = obj.rotateRight(l1, 2001)
PrintLinkedList(l2)

        


