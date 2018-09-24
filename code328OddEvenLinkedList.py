"""
328 Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution:
    # see onenote
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        odd, even = head, dummy

        while even and even.next:
            even.next = odd.next
            even = even.next
            if even and even.next:
                odd.next = even.next
                odd = odd.next

        odd.next = dummy.next

        return head

obj = Solution()
head = ListNode(0)
head.fromList([1, 2, 3, 4, 5])
PrintLinkedList(obj.oddEvenList(head))