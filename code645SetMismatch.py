"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""
# similar problems: 442 Find All Duplicates in an Array
class Solution:
    # tricky O(1) space O(n) time solution from http://www.cnblogs.com/grandyang/p/7324242.html
    # mark corresponding index by turning the number to negative, in this way we know if the index has been visited
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        # first loop to find the duplicated number
        for num in nums:
            i = abs(num) - 1    # find the index corresponding to current value
            if nums[i] < 0:
                res[0] = i + 1  # this index has been visited before, so we find the duplicated number
            else:
                nums[i] *= -1   # mark this index has been visited by changing the number to negative
        
        # second loop to find the index which has not been visited
        for i, num in enumerate(nums):
            if num > 0:
                res[1] = i + 1
                break

        return res

    # my own solution, use set xor operation to find the missing number, then use xor to find the repeat number
    def findErrorNums2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff1, diff2 = 0, 0

        for i in range(len(nums)):
            diff1 ^= (i+1)
            diff2 ^= nums[i]

        diff3 = diff1^diff2 # this is the XOR result of the two numbers
        remain = set(range(1, len(nums)+1))^set(nums)
        b = remain.pop()
        a = diff3^b

        return [a, b]

nums = [1, 2, 2, 4]
print(Solution().findErrorNums(nums))        