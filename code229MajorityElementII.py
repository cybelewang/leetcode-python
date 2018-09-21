"""
229 Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

"""
# Extended Moore Majority algorithm to 2 candidates
class Solution:
    # Best OJ solution, 2-candidate Moore vote algorithm,
    # https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]
    # based on previous java submission.
    def majorityElement2(self, nums):
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
                count1 += 1 # fixed a bug here: forgot to increase count1
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
        c1, c2 = 0, 0
        for num in nums:
            if num == candidate1:
                c1 += 1
            if num == candidate2:
                c2 += 1
        
        res = []
        if c1 > n//3:
            res.append(candidate1)
        if c2 > n//3:
            res.append(candidate2)

        return res
    
test_cases = [[], [1], [1, 1], [1, 2], [1, 1, 2], [1, 2, 3], [2, 2, 1, 3]]
obj = Solution()
for case in test_cases:
    print(case, end = '->')
    print(obj.majorityElement(case))