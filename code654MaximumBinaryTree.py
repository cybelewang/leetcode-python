"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""
# similar problems: 307 Range Sum Query Mutable
from TreeNode import *
class Solution:
    def constructMaximumBinaryTree_OJBest(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if not nums: return None
        stack = []
        for n in nums:
            cur = TreeNode(n)

            while stack and stack[-1].val < n:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]

    # my own solution using segment tree, O(nlogn)
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        index = {num:i for i, num in enumerate(nums)}
        # construct the segment tree
        self.st = [0]*n + nums
        for i in range(n-1, 0, -1):
            self.st[i] = max(self.st[2*i], self.st[2*i+1])

        # construct the max binary tree
        def maxBT(i, j):
            if i < j:
                max_value = self.query(i, j, n) # get the max value in [i, j)
                idx = index[max_value]  # find the index in nums corresponding to max_value
                root = TreeNode(max_value)  # create the root
                root.left = maxBT(i, idx)   # link to left subtree
                root.right = maxBT(idx+1, j)    # link to right subtree

                return root
            else:
                return None

        # main
        return maxBT(0, n)
        
    def query(self, i, j, n):
        """
        use segment tree to query the maximum value from nums[i, j), i inclusive, j exclusive
        n is the length of nums
        """
        i, j = i + n, j + n
        res = -2**31
        while i < j:
            if i & 1:
                res = max(res, self.st[i])
                i += 1
            if j & 1:
                j -= 1
                res = max(res, self.st[j])
            i //= 2
            j //=2

        return res
            
nums = [3,2,1,6,0,5]
PrintTree(Solution().constructMaximumBinaryTree(nums))