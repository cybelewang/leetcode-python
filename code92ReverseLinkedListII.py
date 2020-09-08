"""
92 Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""
from ListNode import *
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        helper = ListNode(0)
        helper.next = head

        pre = helper
        for i in range(m - 1):
            pre = pre.next
        
        # Now pre.next will be the 1st node to be reversed
        head, left, right = pre.next, pre.next, pre.next.next
        for j in range(n- m):
            temp = right.next
            right.next = left
            left = right
            right = temp
        
        pre.next = left
        head.next = right

        return helper.next

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
        fakeHead = ListNode(0)
        fakeHead.next = head
        # find the pre node (whose next is mth node) and the tail node (nth node)
        pre, tail = fakeHead, None
        node = fakeHead # iterator
        for step in range(1, n+1):
            node = node.next
            if step == m - 1:
                pre = node
            if step == n:
                tail = node
        # get the head (mth node)
        head = pre.next
        pre.next = None # disconnect pre and this section of list
        temp = tail.next # temporarily save tail.next to be connected in future
        tail.next = None # disconnect tail with temp
        # reverse the partial list
        pre1, node = None, head
        while node:
            t = node.next
            node.next = pre1
            pre1 = node
            node = t
        # connect pre with the new head (previous tail)
        pre.next = tail
        # connect new tail (previous head) with temp
        head.next = temp
        return fakeHead.next

obj = Solution()
l1 = ListNode(0)
l1.fromList([1,2,3])
l2 = obj.reverseBetween(l1,1,3)
PrintLinkedList(l2)