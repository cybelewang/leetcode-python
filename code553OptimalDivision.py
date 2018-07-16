"""
Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. 
You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. 
Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Note:

The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.
"""
class Solution:
    # tricky problem, help from http://www.cnblogs.com/grandyang/p/6886673.html
    # a/(b/c/d) = a*(c*d)/b, so there is only one optimal division, which put b as denominator and others as numerator
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        strs = [str(num) for num in nums]
        if n > 3:
            strs[1] = '(' + strs[1]
            strs[-1] = strs[-1] + ')'
        
        return '/'.join(strs)

nums = [1000,100,10,2]
print(Solution().optimalDivision(nums))