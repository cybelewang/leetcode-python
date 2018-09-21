from ListNode import *
"""
142 Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow, fast = head, head
        while fast is not None: # bug fixed: should not be "while fast is not None and fast != slow" because fast == slow initally
            fast = fast.next
            if fast is not None:
                fast = fast.next

            slow = slow.next

            if fast == slow:
                break
        
        if fast is None:    # No loop
            return None
        
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

obj = Solution()
l1 = ListNode(0)
l1.fromList([1])
obj.detectCycle(l1)