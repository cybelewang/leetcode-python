"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
# problem 303's solution: update O(n), query O(1)
# segment tree: update O(logn), query O(logn)
# so we use segment tree. For implementation details, see http://codeforces.com/blog/entry/18051
# Binary Indexed Tree?
class NumArray:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # construct segment tree with size 2*len(nums)
        self.length = len(nums)
        self.st = [0]*self.length
        self.st.extend(nums)

        for i in range(self.length-1, 0, -1): # omit st[0] for easy index calculation
            self.st[i] = self.st[2*i] + self.st[2*i+1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if -1 < i < self.length:
            p = i + self.length
            self.st[p] = val
            while p > 1:
                self.st[p//2] = self.st[p] + self.st[p^1]
                p //= 2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        if -1 < i <= j < self.length:
            i += self.length
            j += self.length + 1    # make j exclusive
            while i < j:
                if i & 1:
                    res += self.st[i]
                    i += 1
                if j & 1:
                    j -= 1
                    res += self.st[j]
                i //= 2
                j //= 2
        
        return res


# Your NumArray object will be instantiated and called as such:
nums = list(range(13))
obj = NumArray(nums)
print(obj.sumRange(0, 6))
obj.update(0,1)
print(obj.sumRange(0,6))