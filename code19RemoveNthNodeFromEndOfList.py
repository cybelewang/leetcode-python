from ListNode import ListNode

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    i, left, right = 0, head, head
    while (right.next != None) and (i < n):
        right = right.next
        i += 1
    while (right.next != None):
        right = right.next
        left = left.next
    if left == head:
        return head.next
    else:
        
