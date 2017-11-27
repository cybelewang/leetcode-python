from ListNode import *
from TreeNode import *
"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        
        n, node = 0, head
        while node is not None:
            n += 1
            node = node.next
        
        return self._recursive(head, n)

    def _recursive(self, head, n):
        """
        :type head: ListNode
        n is the length of the list
        :rtype: TreeNode
        """
        if n < 1:
            return None
        half = (n + 1)//2   # half length of the list
        node = head
        for i in range(half-1):
            node = node.next
        
        root = TreeNode(node.val)
        root.left = self._recursive(head, half - 1)
        root.right = self._recursive(node.next, n - half)

        return root

test_case = [1]
ll = ListNode(0)
ll.fromList(test_case)
PrintLinkedList(ll)
obj = Solution()
res = obj.sortedListToBST(ll)
PrintTree(res)