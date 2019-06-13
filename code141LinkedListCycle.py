from ListNode import *
"""
141 Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # a corner case is head->None, both slow and fast will stop after 1 travel
        if head is None or head.next is None:
            return False

        slow, fast = head, head # fast iterator is 2x speed of slow iterator
        while fast is not None:
            # slow iterates 1 node
            slow = slow.next
            # fast iterates 2 nodes, or hit the end
            fast = fast.next
            if fast is not None:
                fast = fast.next
            # check if slow and fast points to the same node
            if slow == fast:    # be careful of None == None, when "head -> None"
                return True

        return False

    # 2nd round solution on 6/10/2019
    def hasCycle2(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False

obj = Solution()
l1 = CreateLinkedList([1, 2])
#l1.fromList([1])
print(obj.hasCycle2(l1))