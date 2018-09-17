"""
24 Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
from ListNode import *
def swap(n1, n2):
    """
    Swap two nodes and return tuple (head, tail)
    :type n1: ListNode
    :type n2: ListNode
    :rtype: (ListNode, ListNode)
    """
    if n2:
        tail = n2.next
        n2.next = n1
        n1.next = tail
        return (n2, n1)
    elif n1:
        n1.next = None
        return (n1, None)
    else:
        return (None, None)

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    helper = ListNode(0)
    helper.next = head
    pre = helper
    while head:
        (newHead, newTail) = swap(head, head.next)
        pre.next = newHead
        if newTail:
            pre = newTail
            head = newTail.next
        else:
            head = None

    return helper.next

l1 = ListNode(0)
l1.fromList([1, 2, 3, 4, 5])
l2 = swapPairs(l1)
PrintLinkedList(l2)