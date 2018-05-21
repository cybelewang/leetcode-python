"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from TreeNode import *
class Solution:

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.target = sum
        self.helper(root)

        return self.count
        
    def helper(self, root):
        """
        get a list of sums including: 
        (1) this node's value (so this node serves as the end) 
        (2) this node's value + left child's sums list (include left child)
        (3) this node's value + right child's sums list (include right child)
        """
        if not root:
            return []
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            res = [root.val]
            if root.val == self.target:
                self.count += 1
            for num in left + right:
                res.append(root.val + num)
                if root.val + num == self.target:
                    self.count += 1

            return res

# pure recursive solution
class Solution2:

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.helper(root, 0, sum)

        return self.count

    def helper(self, node, partial, target):
        """
        recursively iterate all nodes and check if previous sum plus current node can achieve the target. If so, increase the count.
        Then we need to recursively call helper by including current node's value into partial, and not including current's value into partial (this means current node will be new start)
        partial: sum from parent nodes
        target: target number
        """
        if not node:
            return

        if partial + node.val == target:
            # do not exit, we should continue searching
            self.count += 1

        self.helper(node.left, partial + node.val, target) # including this node
        self.helper(node.right, partial + node.val, target) # including this node

        self.helper(node.left, 0, target)  # starting from left child
        self.helper(node.right, 0, target) # starting from right child

null = None
test_case =  [10,5,-3,3,2,null,11,3,-2,null,1]
root = ListToTree(test_case)
print(Solution().pathSum(root, 8))
        