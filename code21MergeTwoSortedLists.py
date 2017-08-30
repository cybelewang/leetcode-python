from ListNode import *

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""
def merge(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    node = head
    while l1 or l2:
        if not l1:
            node.next = l2
            break
        elif not l2:
            node.next = l1
            break
        else:
            if l1.val < l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next

    return head.next


l1, l2 = ListNode(0), ListNode(0)
l1.fromList([1, 3, 5, 7, 9])
l2.fromList([2, 4, 6, 8])
l3 = merge(l2,l1)
PrintLinkedList(l3)