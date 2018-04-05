"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""
class Solution:
    #https://leetcode.com/problems/patching-array/discuss/78488/Solution-+-explanation
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, res, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1
        
        return res

    # naive solution
    def minPatches2(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        exist = [False]*(n+1) # exist[i] indicates if number i can be formed
        build = set()

        for num in nums:
            if 1 <= num <= n:
                exist[num] = True                
                for i in sorted(build):
                    if num + i <= n:
                        exist[num + i] = True
                        build.add(num+i)
                    else:
                        break
                build.add(num)

        i, res = 1, 0
        while i <= n:
            if not exist[i]:
                patch = i
                #print(patch)
                exist[patch] = True
                for j in sorted(build):
                    if patch + j <= n:
                        exist[patch + j] = True
                        build.add(patch + j)
                    else:
                        break
                build.add(patch)

                res += 1
            
            i += 1

        return res

nums = [1, 5, 10]
n = 20
obj = Solution()
print(obj.minPatches(nums, n))