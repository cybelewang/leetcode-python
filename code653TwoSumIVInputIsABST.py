"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
class Solution:
    # similar to two-pointer array solution
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        # stacks to hold the most left and most right tree nodes
        left, right = [], []
        node = root
        while node:
            left.append(node)
            node = node.left

        node = root
        while node:
            right.append(node)
            node = node.right

        small, large = left.pop(), right.pop()
        node = small.right
        while node:
            left.append(node)
            node = node.left

        node = large.left
        while node:
            right.append(node)
            node = node.right

        while small != large:
            sum_ = small.val + large.val
            if sum_ == k:
                return True
            elif sum_ < k:
                small = left.pop()
                node = small.right
                while node:
                    left.append(node)
                    node = node.left
            else:
                large = right.pop()
                node = large.left
                while node:
                    right.append(node)
                    node = node.right

        return False
            

    # recursive solution, O(n) space
    def findTarget2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def helper(root, m, k):
            if not root:
                return False
            # left subtree
            left = helper(root.left, m, k)
            # current node
            if k - root.val in m:
                return True                        
            m.add(root.val)
            # right subtree
            right = helper(root.right, m, k)

            return left or right

        return helper(root, set(), k)