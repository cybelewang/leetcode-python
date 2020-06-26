"""
75 Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
# similar problems: 324 Wiggle Sort II
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i, j, k = 0, len(nums) - 1, 0

        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                while i<=j and nums[i] == 0: i += 1
                k = max(i, k)
            elif nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                while i<=j and nums[j] == 2: j -= 1
            else:
                k += 1

    # 2nd round solution on 9/9/2018
    # my own solution, not one pass
    # left, right are next insertion positions for 0 and 2
    # i, j are iterators along two directions
    # we advance i and decrease j, for nums[i], if it is 0, assign 0 to nums[left], then advance left; if nums[i] is 1, just pass it but do not advance left; if nums[i] is 2, swap with nums[j] and do not advance i
    # similar method for j, but we must be cautious for i == j, we should process it separately
    # finally, assign all index from left to right to 1
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:    return

        n = len(nums)
        left, i, j, right = 0, 0, n-1, n-1
        while i < j:
            if nums[i] == 0:
                nums[left] = 0
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:   # nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[j] == 2:
                nums[right] = 2
                right -= 1
                j -= 1
            elif nums[j] == 1:
                j -= 1
            else:   # nums[j] == 0
                nums[i], nums[j] = nums[j], nums[i]

        if i == j:
            if nums[i] == 0:
                nums[left] = 0
                left += 1
            elif nums[i] == 2:
                nums[right] = 2
                right -= 1


        for k in range(left, right+1):
            nums[k] = 1

    # solution 2 from http://www.cnblogs.com/grandyang/p/4341243.html
    def sortColors3(self, nums):
        i, j, k = 0, 0, len(nums) - 1   # i, k are left and right candidate insertion positions, j is the iterator from 0 to n-1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                # do not need to check nums[j] in next while loop after swap because nums[i] must be 1 if i < j before swap
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
                j -= 1  # trick: need to check nums[j] in next while loop because nums[j] could be 0 after swap
            
            j += 1

    # smart solution! Can be extended to N colors (N is a limited number)
    def sortColors_OJBest(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        for k in range(len(nums)):
            v=nums[k]
            nums[k]=2
            if v<2:
                nums[j]=1
                j+=1
            if v==0:
                nums[i]=0
                i+=1        

    # 3rd solution on 4/25/2019
    # easy to understand solution, but it is not one pass
    # put all 0s to left, all 2s to right, and fill range(left, right+1) with 1
    def sortColors4(self, nums):
        left, right = 0, len(nums)-1
        i, j = left, right
        while i <= j:
            # exchange nums[i] and nums[j]
            if nums[i] == 2 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]

            # put all 0s to left
            if nums[i] == 0:
                nums[left] = 0
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            
            # put all 1s to right
            if nums[j] == 2:
                nums[right] = 2
                right -= 1
                j -= 1
            elif nums[j] == 1:
                j -= 1

        # assign nums[left:right+1] to 1
        for i in range(left, right+1):
            nums[i] = 1


test_cases = [[0, 0], [1, 1], [2, 2], [0, 1, 2], [2,1,2,1], [2,1,1,1], [0, 0, 2, 0, 2, 0, 2, 2],[0, 0, 2, 2, 1, 0, 2, 2]]
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    obj.sortColors3(case)
    print(case)
                
