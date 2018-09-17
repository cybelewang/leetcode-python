"""
25 Reverse Nodes in K Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
from ListNode import *
def reverseKGroup2(head, tail, k):
    """
    reverse a group of k nodes with pre and tail
    :type head: ListNode
    :type tail: ListNode
    :type k: int
    """
    if k < 2:
        return (head, tail)
    node = head

    if k % 2 != 0:
        # k is odd
        for i in range((k-1)//2 - 1):
            node = node.next
        midLeft, mid, midRight = node, node.next, node.next.next
        # keep working on left half
        (leftHead, leftTail) = reverseKGroup2(head, midLeft, k//2)
        # keep working on right half
        (rightHead, rightTail) = reverseKGroup2(midRight, tail, k//2)
        # swap left half and right half
        rightTail.next = mid
        mid.next = leftHead
        # update head and tail
        head = rightHead
        tail = leftTail
    else:
        # k is even
        for i in range((k-1)//2):
            node = node.next
        midLeft, midRight = node, node.next
        # keep working on left half
        (leftHead, leftTail) = reverseKGroup2(head, midLeft, k//2)
        # keep working on right half
        (rightHead, rightTail) = reverseKGroup2(midRight, tail, k//2)
        # swap left half and right half
        rightTail.next = leftHead
        head = rightHead
        tail = leftTail

    return (head, tail)


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    helper = ListNode(0)
    helper.next = head
    pre, tail = helper, helper
    count = 0
    while tail:
        tail = tail.next
        count += 1
        if (count == k) and tail: # bug fixed --- need to reconsider tail if it has been updated. consider the case 1->2->None with k = 3
            nextHead = tail.next # temporarily save the next group's head
            (newHead, newTail) = reverseKGroup2(head, tail, k) # swap this k group nodes
            pre.next = newHead # link the pre node with the new head
            newTail.next = nextHead # link the new tail with the previously saved next group's head
            pre = newTail # update pre node
            head = nextHead # update head node
            tail = newTail # update tail node
            count = 0
    
    return helper.next

l1 = ListNode(0)
l1.fromList([1, 2, 3, 4, 5])
PrintLinkedList(l1)
print()
l2 = reverseKGroup(l1, 3)
PrintLinkedList(l2)
print()
print(CountLinkedList(l2))