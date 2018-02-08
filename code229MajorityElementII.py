"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

"""
# Extended Moore Majority algorithm to 2 candidates
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 1:
            return []

        candidate1, candidate2 = nums[0], nums[0]
        count1, count2 = 0, 0
        for i in range(n):
            # stops at the first different number
            if nums[i] != candidate1:
                break
        else:
            # the entire array contains the same number
            return [candidate1]
        
        # now nums[i] is the first number that is different from candidate1, we assign this number to candidate2
        candidate2, count2 = nums[i], 1
        i += 1

        for j in range(i, n):
            if nums[j] == candidate1:   # case 1: match candidate1, count1+1
                count1 += 1
            elif nums[j] == candidate2: # case 2: match candidate2, count2+1
                count2 += 1
            elif count1 == 0:   # case 3: do not match either candidate, and count1==0, assign candidate1 to this value
                candidate1, count1 = nums[j], 1
            elif count2 == 0:   # case 3: do not match either candidate, and count2==0, assign candidate1 to this value
                candidate2, count2 = nums[j], 1
            else:   # case 4: do not match either candidate, and count1>0, count2>0, decrease both candidates' vote
                count1 -= 1
                count2 -= 1
        
        # 2nd round to check the counts of candidate1 and candidate2
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        res = []
        if count1 > n//3:
            res.append(candidate1)
        if count2 > n//3:
            res.append(candidate2)

        return res
    
test_cases = [[], [1], [1, 1], [1, 2], [1, 1, 2], [1, 2, 3]]
obj = Solution()
for case in test_cases:
    print(case, end = '->')
    print(obj.majorityElement(case))