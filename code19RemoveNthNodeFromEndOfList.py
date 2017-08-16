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

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if n == 0: # should we consider remove 0th node?
        return head

    pre = ListNode(0) # aux head to take care of removing head, tail of a linked list
    pre.next = head

    i, tail = 0, head

    head = pre
    while tail.next != None:
        i += 1
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
    head.printAll()
    print()
    result = removeNthFromEnd(head, 2)
    result.printAll()
    print()
    head = ListNode(0)
    head.fromList(test_case)
    result = removeNthFromEnd(head, 5)
    result.printAll()
    print()
    head = ListNode(0)
    head.fromList(test_case)
    result = removeNthFromEnd(head, 1)
    result.printAll()
    print()
    head = ListNode(0)
    head.fromList(test_case)
    result = removeNthFromEnd(head, 0)
    result.printAll()