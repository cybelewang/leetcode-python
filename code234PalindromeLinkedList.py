"""
234 Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Find the mid node
        fast, slow, count = head, head, 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1

        # Get the right half nodes' head based on odd-length or even-length
        if not fast:
            count *= 2
            right = slow
        else:
            count = 2*count + 1
            right = slow.next
        
        # reverse the right half nodes (if odd length, not including the mid node)
        cur, pre = right, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        right = pre

        # parallel comparison
        for i in range(count//2):
            if head.val != right.val:
                return False
            else:   # bug fixed: forgot to advance pointers
                head = head.next
                right = right.next
        
        return True

       
obj = Solution()
l1 = ListNode(0)
l1.fromList([1,2,2, 1])
print(obj.isPalindrome(l1))