"""
315 Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

"""
from bisect import bisect_left, insort_left

class TreeNodeCount:
    
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 1

class Solution:
    # O(nlogn), construct modified BST with count represents number of nodes <= current node (including current node)
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)        
        count = [0]*n

        if n < 1:
            return count

        def insertNode(root, val):
            thisCount = 0
            while True:
                if val <= root.val:
                    root.count += 1
                    if root.left is None:
                        root.left = TreeNodeCount(val)
                        break
                    else:
                        root = root.left
                else:
                    thisCount += root.count
                    if root.right is None:
                        root.right = TreeNodeCount(val)
                        break
                    else:
                        root = root.right
            
            return thisCount

        root = TreeNodeCount(nums[-1])
        for i in range(n-2, -1, -1):
            count[i] = insertNode(root, nums[i])

        return count

    # merge sort solution
    # merge from large to small
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
    def countSmaller3(self, nums):
        res = [0]*len(nums)
        def sort(arr):
            n = len(arr)
            if n < 2:
                return arr
            left, right = sort(arr[:n//2]), sort(arr[n//2:])
            for i in range(n-1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    res[left[-1][0]] += len(right)
                    arr[i] = left.pop()
                else:
                    arr[i] = right.pop()
            return arr
        
        sort(list(enumerate(nums)))
        return res

    # use an extra list to save each number in order. The insertion position tells how many numbers are smaller than the inserted number.
    # worst case O(n^2), a little better than brutal force solution 
    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, res = [], []
        for num in reversed(nums):
            res.append(bisect_left(a, num))
            insort_left(a, num)
        
        return res[::-1]
    
obj = Solution()
test_cases = [[], [1], [1, 2], [7, 0, 5, 2, 3, 1]]
for case in test_cases:
    print(obj.countSmaller(case))