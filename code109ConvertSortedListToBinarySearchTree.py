from ListNode import *
from TreeNode import *
"""
109 Convert Sorted List to Binary Search Tree

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
    # trick solution by simulating inorder traversal
    # time O(n), space O(logn)
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convert(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l + r) // 2
            left = convert(l, mid-1)            
            root = TreeNode(head.val)
            root.left = left
            head = head.next            
            root.right = convert(mid+1, r)
            return root
            
        n, node = 0, head
        while node:
            n += 1
            node = node.next       
        
        return convert(0, n - 1)
    # O(nlogn) time, O(logn) space solution
    def sortedListToBST2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        n, node = 0, head
        while node:
            n += 1
            node = node.next
        
        sentinel = ListNode(0)
        sentinel.next = head
        node = sentinel
        for _ in range(n//2):
            node = node.next
        
        temp = node.next
        node.next = None
        
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(sentinel.next)
        root.right = self.sortedListToBST(temp.next)
        
        return root

test_case = [1]
ll = ListNode(0)
ll.fromList(test_case)
PrintLinkedList(ll)
obj = Solution()
res = obj.sortedListToBST(ll)
PrintTree(res)