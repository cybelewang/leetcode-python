"""
327 Count of Range Sum

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""
class Solution:
    # OJ Best solution, also see C++'s solution using multiset
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        first = [0]
        for c in nums:
            first.append(first[-1] + c)
            
        def search(lo, hi):
            
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            
            count = search(lo, mid) + search(mid, hi)
            
            i, j = mid, mid
            for left in first[lo: mid]:
                
                while i < hi and first[i] - left < lower:
                    i += 1
                
                while j < hi and first[j] - left <= upper:
                    j += 1
                    
                count += j - i
                
            first[lo:hi] = sorted(first[lo:hi])
            
            return count
        
        return search(0, len(first))

    # https://leetcode.com/problems/count-of-range-sum/discuss/77990/Share-my-solution
    def countRangeSum2(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        sums = [0]  # sums[i] is the sum from nums[0] to nums[i-1]
        for num in nums:
            sums.append(sums[-1] + num)
        
        return self.countWhileMergeSort(sums, 0, n+1, lower, upper)

    def countWhileMergeSort(self, sums, start, end, lower, upper):
        if end - start < 2:
            return 0
        mid = (start + end)//2
        # recursively sort left half and right half
        count = self.countWhileMergeSort(sums, start, mid, lower, upper) + self.countWhileMergeSort(sums, mid, end, lower, upper)
        j, k, t = mid, mid, mid

        cache = []
        for i in range(start, mid):
            # find the lower limit
            while k < end and sums[k] - sums[i] < lower:
                k += 1
            # find the upper limit
            while j < end and sums[j] - sums[i] <= upper:
                j += 1
            # In the right side, copy all sums[t] which is < sums[i] to cache
            while t < end and sums[t] < sums[i]:
                cache.append(sums[t])
                t += 1
            # include sums[i] itself
            cache.append(sums[i])
            count += j - k
        # copy cache back to sums so this part is sorted
        sums[start:start+len(cache)] = cache

        return count

nums = [-2, 5, -1]
obj = Solution()
print(obj.countRangeSum(nums, -2, 2))            