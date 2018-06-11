"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, 
please find out a way you can make one square by using up all those matchsticks. 
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. 
Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""
# similar to 416 partition equal subset sum, this problem requires 4 subsets with equal length
class Solution:
    # OJ's better solution
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse=True)
        if len(nums) < 4:
            return False
        total = sum(nums)
        if total % 4 != 0:
            return False
        target = total / 4
        if any(n > target for n in nums):
            return False
        return self.dfs([target] * 4, 0, nums)

    def dfs(self, lefts, idx, nums):
        if idx == len(nums):
            return True
        n = nums[idx]
        used = set()
        for i, left in enumerate(lefts):
            if left >= n and left not in used:
                lefts[i] -= n
                if self.dfs(lefts, idx + 1, nums):
                    return True
                lefts[i] += n
                used.add(left)
        return False

    # not solved, help from http://www.cnblogs.com/grandyang/p/6238425.html
    # sort nums in reversed order, allocate 4 buckets, then iterate all buckets, for each bucket, try to add from the largest if the sum is <= target, then recursively call dfs
    # after each recursive call, remove the added number from the bucket to test all cases
    def makesquare2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False

        sum_ = sum(nums)
        length = sum_//4
        if sum_ % 4 != 0 or nums[0] > length:
            return False

        nums.sort(reverse = True)

        return self.dfs2(nums, [0]*4, 0, length)

    def dfs2(self, nums, sums, pos, target):
        if pos >= len(nums):
            return all(x == target for x in sums)
        for i in range(4):
            if sums[i] + nums[pos] > target: 
                continue
            sums[i] += nums[pos]
            if self.dfs(nums, sums, pos + 1, target):
                return True
            sums[i] -= nums[pos]

        return False

obj = Solution()
#nums = [8,16,24,32,40,48,56,64,72,80,88,96,104,112,60]
nums = [12,12,12,12,12,12,12,12,12,12,12,12,12]
print(obj.makesquare(nums))