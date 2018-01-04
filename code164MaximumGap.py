"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
from math import ceil

class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        # get min and max values
        minVal, maxVal = nums[0], nums[0]
        for num in nums:
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)
        
        # Between min and max the total gap is (max - min) and there are (N-1) slots
        # The average gap per slot is (max - min)/(N-1), this might be a double value
        # The max gap must be >= ceiling[(max - min)/(N-1)], otherwise (N-1)*(max gap) cannot fill the total gap (max-min)
        # We can set up (N-1) bucks and use ceiling[(max - min)/(N-1)] as the bucket bin size
        # Each bucket starts (including) from [min + (k-1)*(bin size)], and ends at [min + k*(bin size)] (not including)
        # We then fill the (N-1) buckets with (N-2) numbers (all numbers except min and max), so at least one bucket must be empty
        # The gap between any two numbers in the same bucket must be <= bin size, so we only need to keep track the min and max in each bucket

        N = len(nums)
        binsize = ceil((maxVal - minVal)/(N-1))

        # create buckets
        buckets = [None for i in range(N-1)]

        # put numbers into buckets
        for num in nums:
            if num != minVal and num != maxVal:
                i = (num - minVal)//binsize # calculate the index of corresponding bucket
                if buckets[i] is None:
                    buckets[i] = (num, num) # put new tuple into bucket
                else:
                    buckets[i][0] = min(buckets[i][0], num) # update min in bucket
                    buckets[i][1] = max(buckets[i][1], num) # update max in bucket
        
        res = 0
        # scan buckets and get the max gap
        for bucket in buckets:
            if bucket is not None:
                res = max(res, bucket[0] - minVal)
                minVal = bucket[1]
        
        # don't forget the gap between maxVal and last bucket
        res = max(res, maxVal - minVal)

        return res

obj = Solution()
test_cases = [[], [1], [1, 2, 3], [1, 101], [-2**31, 2**31-1], [1, 4, 2, 7]]
for case in test_cases:
    print(case, end=' -> ')
    print(obj.maximumGap(case))