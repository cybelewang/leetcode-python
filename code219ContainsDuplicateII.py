"""
219 Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""
class Solution:
    # use a sliding window with size (k+1) and then keep poping left element from a hashset while adding right element into the hashset
    # note k can be MAX_INT
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2 or k < 1:  # bug fixed: previously used condition k >= len(nums) to return False, which was wrong. k could be a very large number.
            return False

        n, records = len(nums), set()
        for j in range(min(k+1, n)):
            if nums[j] in records:
                return True
            else:
                records.add(nums[j])
        
        i = 0
        for j in range(k+1, n):
            records.discard(nums[i])
            i += 1
            if nums[j] in records:
                return True
            else:
                records.add(nums[j])

        return False

    # 2nd round solution on 2/20/2019
    def containsNearbyDuplicate2(self, nums, k):
        if len(nums) < 2 or k < 1:
            return False

        index = {}
        for i, num in enumerate(nums):
            if num in index:
                if i - index[num] <= k:
                    return True
            index[num] = i
        
        return False

test_case = [1, 2, 1]
obj = Solution()
print(obj.containsNearbyDuplicate2(test_case, 2**31-1))    