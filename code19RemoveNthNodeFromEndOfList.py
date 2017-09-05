from ListNode import *

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

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    pre = ListNode(0)
    pre.next = head

    node, tail = pre, pre
    for i in range(n):
        tail = tail.next
    
    while tail:
        tail = tail.next
        node = node.next
    
    rm = node.next
    if rm:
        node.next = rm.next

    return pre.next

def removeNthFromEnd2(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    pre = ListNode(0) # aux head to take care of removing head, tail of a linked list
    pre.next = head

    i, tail = 0, head

    head = pre
    while tail.next != None:
        i += 1  # ith node from the head
        tail = tail.next
        if i >= n:  # bug fixed here. old statement "i > n"
            pre = pre.next
    
    # link pre to the node after the removed node
    node = pre.next
    pre.next = node.next

    return head.next

test_cases = [[1, 2, 3, 4, 5]]
for test_case in test_cases:
    head = ListNode(0)
    head.fromList(test_case)
    PrintLinkedList(head)
    print()
    result = removeNthFromEnd(head, 2)
    PrintLinkedList(result)
    print()
    head = ListNode(0)
    head.fromList(test_case)
    result = removeNthFromEnd(head, 5)
    PrintLinkedList(result)
    print()
    head = ListNode(0)
    head.fromList(test_case)
    result = removeNthFromEnd(head, 1)
    PrintLinkedList(result)
    print()
